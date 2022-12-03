from unittest import TestCase
from check_answers import check_player_answer


class TestCheckPlayerAnswer(TestCase):
    def test_check_player_answer_true(self):
        self.assertEqual(True, check_player_answer('10', '10'))

    def test_check_player_answer_false(self):
        self.assertEqual(False, check_player_answer('7', '17'))

    def test_check_player_answer_empty_string_true(self):
        self.assertEqual(True, check_player_answer('', ''))

    def test_check_player_answer_empty_string_false(self):
        self.assertEqual(False, check_player_answer('', '3'))

    def test_check_player_answer_string_of_letters_true(self):
        self.assertEqual(True, check_player_answer('test', 'test'))

    def test_check_player_answer_string_of_letters_false(self):
        self.assertEqual(False, check_player_answer('test', 'different'))
