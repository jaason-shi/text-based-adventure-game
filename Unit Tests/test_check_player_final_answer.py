from unittest import TestCase
from game import check_player_final_answer


class TestCheckPlayerFinalAnswer(TestCase):
    def test_check_player_final_answer_true(self):
        self.assertEqual(True, check_player_final_answer('21'))

    def test_check_player_final_answer_false(self):
        self.assertEqual(False, check_player_final_answer('14'))

    def test_check_player_final_answer_empty_string_false(self):
        self.assertEqual(False, check_player_final_answer(''))

    def test_check_player_final_answer_negative_integer_false(self):
        self.assertEqual(False, check_player_final_answer('-4'))
