# def game():  # called from main
#     rows = 10
#     columns = 10
#     board = make_board(rows, columns)
#     character = make_character("Player name")
#     achieved_goal = False
#     while not achieved_goal:
#         # Tell the user where they are
#         describe_current_location(board, character)


# THIS ONE  ##

# def make_board(rows, columns):
#     board_dict = {}
#     for row in range(rows):
#         for column in range(columns):
#             board_dict[(row, column)] = "x"
#     return board_dict
#
#
# print(make_board(10, 10))


# def character_name() -> str:
#     print("Please enter a name for your character: ")
#     return input()
#
#
# def make_character(name: str) -> dict:
#     return {'name': name,
#             'level': 1,
#             'attempts': 3,
#             'XP': 0,
#             'x-coordinate': 10,
#             'y-coordinate': 10}
#
#
# print(make_character(character_name()))



## INFO
# rows = 10
# columns = 10
# board = make_board(rows, columns)
#
# def get_user_choice()


# character = make_character("Player name")


# def describe_current_location(board):
#     for x in range(rows):
#         for y in range(columns):
#             print(board[(x, y)], end=' ')
#         print()
#
#
# print(describe_current_location(board))



# # insert data into dictionary
# dict1 = {(0, 0): 'Samuel', (0, 1): 21, (0, 2): 'Data structures',
#          (1, 0): 'Richie', (1, 1): 20, (1, 2): 'Machine Learning',
#          (2, 0): 'Lauren', (2, 1): 21, (2, 2): 'OOPS with Java'
#          }
#
# # Iterate through the dictionary
# # to print the data.
# for i in range(3):
#
#     for j in range(3):
#         print(dict1[(i, j)], end='   ')
#
#     print()

# print(make_board(10, 10))


# print(make_character())


# def describe_current_location(board, character):
#     for key in board:
#         print("x" * rows)
#
#     # print(board)


# Create a dictionary
# k = 0
# d = {}
# for row in range(10):
#      for column in range(10):
#          d[k] = (row, column)
#          k += 1
#
# print(d)

import json
from random import randint


def make_board(rows: int, columns: int) -> dict:
    board_dict = {}
    get_rooms = open('rooms.json', 'r')
    rooms = json.load(get_rooms)
    for row in range(rows):
        for column in range(columns):
            if row == 0 and column == 0:
                board_dict[(row, column)] = rooms["rooms_list"][randint(0, 9)]
            elif row == 1 and column == 1:
                board_dict[(row, column)] = rooms["rooms_list"][randint(0, 9)]
            elif row == 2 and column == 2:
                board_dict[(row, column)] = rooms["rooms_list"][randint(0, 9)]
            elif row == 3 and column == 3:
                board_dict[(row, column)] = rooms["rooms_list"][randint(0, 9)]
            elif row == 4 and column == 4:
                board_dict[(row, column)] = rooms["rooms_list"][randint(0, 9)]
            # else:
            #     board_dict[(row, column)] = {'room': 'hallway'}
    return board_dict


print(make_board(10, 10))