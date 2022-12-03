import json
# import io
# from random import randint
# from game import character_name, make_character

import json
from random import randint
from game import make_character

test_character = make_character('test')


def make_board(rows, columns):
    get_rooms = open('rooms.json', 'r')
    rooms = json.load(get_rooms)

    board_dict = {}

    for row in range(rows):
        for column in range(columns):
            board_dict[(row, column)] = 'hallway'

    for row in range(1, rows):
        if row >= 3:
            board_dict[randint(0, 9), row] = rooms["rooms_list"][randint(0, 9)]['room']
        if row <= 8:
            board_dict[randint(0, 9), row] = rooms["rooms_list"][randint(0, 9)]['room']
        if row > 3:
            board_dict[randint(0, 9), row] = rooms["rooms_list"][randint(0, 9)]['room']
        if row > 8:
            board_dict[randint(0, 9), row] = rooms["rooms_list"][randint(0, 9)]['room']
    return board_dict


def print_board(board, rows, columns, character):
    character_location = (character['x-coordinate'], character['y-coordinate'])
    for row in range(rows):
        for column in range(columns):
            current_location = board[(row, column)]
            if (row, column) == character_location:
                print("🧍", end='')
            elif current_location == 'hallway':
                print("🏫", end='')
            elif current_location != 'hallway':
                print("📚", end='')
        print()


def move_character(character: dict, player_movement: int) -> None:
    if player_movement == 1:
        character['y-coordinate'] -= 1
    if player_movement == 2:
        character['y-coordinate'] += 1
    if player_movement == 3:
        character['x-coordinate'] -= 1
    if player_movement == 4:
        character['x-coordinate'] += 1

def get_user_choice(choices: list) -> int:
    """
    Return the player's inputted choice.

    :param choices: a list
    :precondition: choices must be a list of possible options for a player to choose from
    :postcondition: correctly returns an integer that is the player's choice
    :return: an integer representing the player's chosen option
    """
    print("Where would you like to go?")
    for number, choice in enumerate(choices, 1):
        print(number, choice)
    player_choice = int(input("Please enter a number to move: "))
    if 1 <= player_choice <= len(choices):
        return player_choice
    else:
        print("That doesn't work! Please try again.")


print_board(make_board(10, 10), 10, 10, test_character)





#
# get_riddles = open('riddles.json', 'r')
# riddles = json.load(get_riddles)
# # for riddle in riddles['riddles_list']:
#     # print(riddle)
#
#
# # def create_room():
# #     row = 10
# #     column = 10
# #     get_rooms = open('rooms.json', 'r')
# #     rooms = json.load(get_rooms)
# #     random_number = randint(0, 9)
# #     room = rooms["rooms_list"][random_number]
# #     if row == 0 and column == 0:
# #         board_dict[(row, column)] = room
# #         # return room[random_index]['rooms']
# #
# # print(create_room())
# # for room in rooms['rooms_list']:
# #     print(room)
#
# get_riddles.close()
#
#
# def make_character(name: str) -> dict:
#     return {'name': name,
#             'level': 1,
#             'attempts': 3,
#             'XP': 0,
#             'x-coordinate': 9,
#             'y-coordinate': 1}
#
# # def make_board(rows, columns):
# #     board = {}
# #     for row in range(rows):
# #         for column in range(columns):
# #             board[(row, column)] = "Johnson"
# #             if column == 1:
# #                 print("\n")
# #             print(board)
# #     # print(row, column)# ["Welcome to the pit of doom", None]
# #     return board
# #
# # print(make_board(10,10))
#
# #
# def make_board(rows: int, columns: int) -> dict:
#     board_dict = {}
#     get_rooms = open('rooms.json', 'r')
#     rooms = json.load(get_rooms)
#     hallway = {'room': 'hallway'}
#     for row in range(rows):
#         for column in range(columns):
#             if row == randint(0, 9) or column == randint(0, 9):
#                 board_dict[(row, column)] = rooms["rooms_list"][randint(0, 9)]
#             else:
#                 board_dict[(row, column)] = hallway
#     return board_dict
#
#
# riddle_number = randint(0, 12)
#
#
# def make_riddle(character: dict, board: dict) -> str:
#     get_riddles = open('riddles.json', 'r')
#     riddles = json.load(get_riddles)
#     current_character_coordinate = (character['x-coordinate'], character['y-coordinate'])
#     current_room = board[current_character_coordinate]['room']
#     if current_room == 'hallway':
#         return riddles['riddles_list'   ][riddle_number]["riddles"]
#
#
# def get_player_answer() -> str:
#     print("Please enter your answer here: ")
#     return input()
#
#
# def get_correct_answer() -> str:
#     correct_answer = riddles['riddles_list'][riddle_number]["answer"]
#     return correct_answer
#
#
# def check_player_answer(player_answer: str, correct_answer: str) -> bool:
#     if player_answer == correct_answer:
#         return True
#     else:
#         return False
#
#
#
# def player_is_correct(character:dict):
#     print("Correct! You have gained 10 XP")
#     character['XP'] += 10
#     character['attempts'] -= 1
#     if character['XP'] == 10:
#         character["level"] += 1
#         character["attempts"] += 3
#     elif character['XP'] == 30:
#         character["level"] += 1
#         character["attempts"] += 3
#     elif character['XP'] == 60:
#         character["level"] += 1
#         character["attempts"] += 3
#
#
# def player_is_wrong(character:dict):
#     print("You got a 0 on the quiz.")
#     character['attempts'] -= 1
#
#
# def no_more_attempts(character:dict):
#     if character['attempts'] == 0:
#         print('You dropped out of the academy.')
#
#
# make two functions: one for true with level up; one for false with while loop
#  while player_answer is not correct_answer, character attempt -1, etc
#
#
#                 if player answer is correct answer
#                         do the level up stuff
#                         break loop
#                 if player answer is not correct answer
#                         keep running the loop
#                         until attempts = 0
#
#
#
#
#
