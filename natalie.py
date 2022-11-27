# def game():  # called from main
#     rows = 10
#     columns = 10
#     board = make_board(rows, columns)
#     character = make_character("Player name")
#     achieved_goal = False
#     while not achieved_goal:
#         # Tell the user where they are
#         describe_current_location(board, character)


def make_character():
    character_name = input("Please enter a name for your character: ")
    return {'name': character_name, 'level': 1, 'attempts': 3, 'XP': 0,
            "X-coordinate": 0, "Y-coordinate": 0}


print(make_character())


# def make_board(rows, columns):
#     board = {}
#     for row in range(rows):
#         for column in range(columns):
#             board[(row, column)] = "x"
#     return board
#
#
# print(make_board(10, 10))


# def describe_current_location(board):
#     board += '\n'
#     # character = 1, 0
#     print(board)
#
#
# print(describe_current_location(10, 10))
