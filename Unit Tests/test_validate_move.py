from unittest import TestCase
from movement import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_direction_one_y_coordinate_zero(self):
        test_character = {'Name': 'Chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 0, 'y-coordinate': 0}
        direction = 1
        expected = False
        actual = validate_move(10, 10, test_character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_direction_one_y_coordinate_not_zero(self):
        test_character = {'Name': 'Chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 0, 'y-coordinate': 3}
        direction = 1
        expected = True
        actual = validate_move(10, 10, test_character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_direction_two_y_coordinate_not_nine(self):
        test_character = {'Name': 'Chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 0, 'y-coordinate': 3}
        direction = 2
        expected = True
        actual = validate_move(10, 10, test_character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_direction_two_y_coordinate_nine(self):
        test_character = {'Name': 'Chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 0, 'y-coordinate': 9}
        direction = 2
        expected = False
        actual = validate_move(10, 10, test_character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_direction_three_x_coordinate_zero(self):
        test_character = {'Name': 'Chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 0, 'y-coordinate': 9}
        direction = 3
        expected = False
        actual = validate_move(10, 10, test_character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_direction_three_x_coordinate_not_zero(self):
        test_character = {'Name': 'Chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 3, 'y-coordinate': 9}
        direction = 3
        expected = True
        actual = validate_move(10, 10, test_character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_direction_four_x_coordinate_nine(self):
        test_character = {'Name': 'Chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 9, 'y-coordinate': 9}
        direction = 4
        expected = False
        actual = validate_move(10, 10, test_character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_direction_four_x_coordinate_not_nine(self):
        test_character = {'Name': 'Chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 8, 'y-coordinate': 9}
        direction = 4
        expected = True
        actual = validate_move(10, 10, test_character, direction)
        self.assertEqual(expected, actual)
