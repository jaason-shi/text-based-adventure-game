import json
import io


get_riddles = open('riddles.json', 'r')
riddles = json.load(get_riddles)
# for riddle in riddles.values():
print(riddles)

get_rooms = open('rooms.json', 'r')
rooms = json.load(get_rooms)
# for room in rooms.values():
print(rooms)

get_riddles.close()
print(type(riddles))





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


