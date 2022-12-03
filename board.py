import json
from random import randint


def make_board(rows: int, columns: int) -> dict:
    """
    Create dictionary to represent the game board with given number of rows and columns.

    :param rows: an integer
    :param columns: an integer
    :precondition: rows must be a positive non-zero integer
    :precondition: columns must be a positive non-zero integer
    :postcondition: make a board of size row x column
    :postcondition: the keys in the dictionary are a tuple representing coordinates of the board as (rows, columns)
    :postcondition: the value of the dictionary represents the location which is either a hallway or a room
    :postcondition: rooms are taken from the rooms.json file and are randomly assigned to keys in the dictionary
    :postcondition: rows and columns are unchanged
    :return: a dictionary that has hallways and rooms from the rooms.json file for every tile in the game
    """
    get_rooms = open('rooms.json', 'r')
    rooms = json.load(get_rooms)

    board_dict = {}

    for row in range(rows):
        for column in range(columns):
            board_dict[(row, column)] = 'hallway'

    for row in range(1, rows):
        if row >= 3:
            board_dict[row, randint(0, 9)] = rooms["rooms_list"][randint(0, 9)]['room']
        if row <= 8:
            board_dict[row, randint(0, 9)] = rooms["rooms_list"][randint(0, 9)]['room']
        if row > 3:
            board_dict[row, randint(0, 9)] = rooms["rooms_list"][randint(0, 9)]['room']
        if row > 8:
            board_dict[row, randint(0, 9)] = rooms["rooms_list"][randint(0, 9)]['room']
    return board_dict


def print_board(board: dict, rows: int, columns: int, character: dict) -> None:
    """
    Print board that shows the location of each tile with emojis, and where the character is located on the board.

    👹represents the character, 🏫 represents the hallways, and 📘 represents a room.

    :param board: a dictionary
    :param rows: an integer
    :param columns: an integer
    :param character: a dictionary
    :precondition: board must be a dictionary representing the current game board
    :precondition: rows must be a positive non-zero integer
    :precondition: columns must be a positive non-zero integer
    :precondition: character must be a dictionary with the attribute keys of 'x-coordinate' and 'y-coordinate'
    :postcondition: prints game board that shows the tiles where there are hallways, rooms, and a character
    :postcondition: the board dictionary is unchanged
    :postcondition: rows and columns are unchanged
    :postcondition: the character dictionary is unchanged
    """
    character_location = (character['x-coordinate'], character['y-coordinate'])
    for column in range(columns):
        for row in range(rows):
            current_location = board[(row, column)]
            if (row, column) == character_location:
                print("👹", end='')
            elif current_location == 'hallway':
                print("🏫", end='')
            elif current_location != 'hallway':
                print("📘", end='')
        print()
