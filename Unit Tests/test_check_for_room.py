from unittest import TestCase
from game import check_for_room


class TestCheckForRoom(TestCase):
    def test_check_for_room_character_not_in_room(self):
        test_character = {'Name': 'chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 0, 'y-coordinate': 0}
        test_board = {(0, 0): 'hallway', (0, 1): 'art room'}
        expected = False
        actual = check_for_room(test_character, test_board)
        self.assertEqual(expected, actual)

    def test_check_for_room_is_false_character_is_in_room(self):
        test_character = {'Name': 'chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 0, 'y-coordinate': 1}
        test_board = {(0, 0): 'hallway', (0, 1): 'art room'}
        expected = True
        actual = check_for_room(test_character, test_board)
        self.assertEqual(expected, actual)
