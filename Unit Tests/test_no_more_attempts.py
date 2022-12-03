from unittest import TestCase
from game import no_more_attempts


class TestNoMoreAttempts(TestCase):
    def test_no_more_attempts_with_zero(self):
        expected = True
        actual = no_more_attempts(
            {'Name': 'chris', 'Grade': 1, 'Attempts': 0, 'XP': 10, 'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)

    def test_no_more_attempts_with_positive(self):
        expected = False
        actual = no_more_attempts(
            {'Name': 'chris', 'Grade': 1, 'Attempts': 2, 'XP': 10, 'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)

    def test_no_more_attempts_with_negative(self):
        expected = False
        actual = no_more_attempts(
            {'Name': 'chris', 'Grade': 1, 'Attempts': -2, 'XP': 10, 'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)
