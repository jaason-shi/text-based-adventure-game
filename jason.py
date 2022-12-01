import json
import io
from random import randint

def make_riddle(character: dict, board: dict) -> str:
    get_riddles = open('riddles.json', 'r')
    riddles = json.load(get_riddles)
    character_coordinate = (character['x-coordinate'], character['y-coordinate'])
    character_location_on_board = board[character_coordinate]['room']
    if character_location_on_board != 'hallway':
        return
    riddle = riddles['riddles_list']
    get_riddles.close()
    return riddle

    #     (riddles['riddles_list'][randint(0, 12)])
print(make_riddle())








if character_has_leveled():
    execute_glow_up_protocol()

# boolean value if riddle has been completed

if True:
    xp + 10
    attempts - 1
    if character xp = 10:
        character level + 1
        attempts + 3
    elif character xp = 20:
        character level + 1
        attempts + 3
    elif character xp = 30:
        character level + 1
        attempts + 3
else:
    attempt - 1
    continue() ?


#   weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee









# def create_room():
#     row = 10
#     column = 10
#     get_rooms = open('rooms.json', 'r')
#     rooms = json.load(get_rooms)
#     random_number = randint(0, 9)
#     room = rooms["rooms_list"][random_number]
#     if row == 0 and column == 0:
#         board_dict[(row, column)] = room
#         # return room[random_index]['rooms']
#
# print(create_room())
# for room in rooms['rooms_list']:
#     print(room)


# def make_board(rows, columns):
#     board = {}
#     for row in range(rows):
#         for column in range(columns):
#             board[(row, column)] = "Johnson"
#             if column == 1:
#                 print("\n")
#             print(board)
#     # print(row, column)# ["Welcome to the pit of doom", None]
#     return board
#
# print(make_board(10,10))

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
# current_room = board[current_character_coordinate]['room']
# there_is_a_challenge = check_for_challenge()
