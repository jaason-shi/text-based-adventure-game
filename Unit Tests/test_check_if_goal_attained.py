from unittest import TestCase
from game import check_if_goal_attained


class TestCheckIfGoalAttained(TestCase):
    def test_check_if_goal_attained_with_grade_three(self):
        expected = True
        actual = check_if_goal_attained(
            {'Name': 'chris', 'Grade': 3, 'Attempts': 2, 'XP': 0, 'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_with_grade_zero(self):
        expected = False
        actual = check_if_goal_attained(
            {'Name': 'chris', 'Grade': 0, 'Attempts': 0, 'XP': 0, 'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_with_grade_negative(self):
        expected = False
        actual = check_if_goal_attained(
            {'Name': 'chris', 'Grade': -1, 'Attempts': 2, 'XP': 0, 'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)