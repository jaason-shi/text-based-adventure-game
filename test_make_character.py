from unittest import TestCase
from game import make_character


class TestMakeCharacter(TestCase):
    def test_make_character_empty_string(self):
        expected = {'Name': '', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 5, 'y-coordinate': 5}
        actual = make_character('')
        self.assertEqual(expected, actual)

    def test_make_character_string_all_lower_case(self):
        expected = {'Name': 'Chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 5, 'y-coordinate': 5}
        actual = make_character('chris')
        self.assertEqual(expected, actual)

    def test_make_character_string_all_upper_case(self):
        expected = {'Name': 'Chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 5, 'y-coordinate': 5}
        actual = make_character('CHRIS')
        self.assertEqual(expected, actual)

    def test_make_character_string_first_letter_capitalized(self):
        expected = {'Name': 'Chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 5, 'y-coordinate': 5}
        actual = make_character('Chris')
        self.assertEqual(expected, actual)

    def test_make_character_string_of_numbers(self):
        expected = {'Name': '1234', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 5, 'y-coordinate': 5}
        actual = make_character('1234')
        self.assertEqual(expected, actual)

    def test_make_character_string_of_numbers_and_letters(self):
        expected = {'Name': 'Abc123', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 5, 'y-coordinate': 5}
        actual = make_character('abc123')
        self.assertEqual(expected, actual)
