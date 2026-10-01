"""Regression cases for the structural supervisor gates."""

import copy
import json
import unittest
from pathlib import Path

from supervise import validate


SAMPLE = Path(__file__).resolve().parent.parent / "references" / "rt-001-audit.json"


class SupervisorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample = json.loads(SAMPLE.read_text(encoding="utf-8"))

    def case(self):
        return copy.deepcopy(self.sample)

    def test_sample_passes_all_gates(self):
        for stage in (1, 2, 3):
            with self.subTest(stage=stage):
                self.assertEqual(validate(self.case(), stage), [])

    def test_missing_director_decision_fails_gate_one(self):
        case = self.case()
        case["direction"]["shot_consequences"] = []
        self.assertTrue(any("shot_consequences" in error for error in validate(case, 1)))

    def test_missing_action_handoff_fails_gate_one(self):
        case = self.case()
        case["roles"]["action"]["status"] = "not_applicable"
        self.assertTrue(any("roles.action" in error for error in validate(case, 1)))

    def test_missing_storyboard_handoff_fails_gate_two(self):
        case = self.case()
        case["roles"]["storyboard"]["status"] = "missing"
        self.assertTrue(any("roles.storyboard" in error for error in validate(case, 2)))

    def test_broken_timing_fails_gate_two(self):
        case = self.case()
        case["shots"][1]["start_sec"] = 2.5
        self.assertTrue(any("gap or overlap" in error for error in validate(case, 2)))

    def test_missing_camera_trace_fails_gate_three(self):
        case = self.case()
        case["outputs"]["video_prompts"][0]["evidence"]["camera"] = "imaginary crane move"
        self.assertTrue(any("evidence.camera" in error for error in validate(case, 3)))

    def test_missing_locked_dialogue_fails_gate_three(self):
        case = self.case()
        for section in case["outputs"]["video_prompts"]:
            section["text"] = section["text"].replace("快了，上面就是凉亭。", "快到了。")
        self.assertTrue(any("locked dialogue L2" in error for error in validate(case, 3)))


if __name__ == "__main__":
    unittest.main()
