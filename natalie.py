import json
import io
from random import randint
from game import character_name, make_character

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


get_riddles = open('riddles.json', 'r')
riddles = json.load(get_riddles)
# for riddle in riddles['riddles_list']:
    # print(riddle)


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

get_riddles.close()


def make_character(name: str) -> dict:
    return {'name': name,
            'level': 1,
            'attempts': 3,
            'XP': 0,
            'x-coordinate': 9,
            'y-coordinate': 1}

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

#
def make_board(rows: int, columns: int) -> dict:
    board_dict = {}
    get_rooms = open('rooms.json', 'r')
    rooms = json.load(get_rooms)
    hallway = {'room': 'hallway'}
    for row in range(rows):
        for column in range(columns):
            if row == randint(0, 9) or column == randint(0, 9):
                board_dict[(row, column)] = rooms["rooms_list"][randint(0, 9)]
            else:
                board_dict[(row, column)] = hallway
    return board_dict


riddle_number = randint(0, 12)


def make_riddle(character: dict, board: dict) -> str:
    get_riddles = open('riddles.json', 'r')
    riddles = json.load(get_riddles)
    current_character_coordinate = (character['x-coordinate'], character['y-coordinate'])
    current_room = board[current_character_coordinate]['room']
    if current_room == 'hallway':
        return riddles['riddles_list'][riddle_number]["riddles"]


def get_player_answer() -> str:
    print("Please enter your answer here: ")
    return input()


def get_correct_answer() -> str:
    correct_answer = riddles['riddles_list'][riddle_number]["answer"]
    return correct_answer


def check_player_answer(player_answer: str, correct_answer: str, character: dict) -> None:
    if player_answer == correct_answer:
        print("Correct! You have gained 10 XP")
        character['XP'] += 10
        character['attempts'] -= 1
        if character['XP'] == 10:
            character["level"] += 1
            character["attempts"] += 3
            return True
        elif character['XP'] == 30:
            character["level"] += 1
            character["attempts"] += 3
            return True
        elif character['XP'] == 60:
            character["level"] += 1
            character["attempts"] += 3
            return True
    else:
        print("Wrong answer")
        character["attempts"] -= 1
        return False




def game():
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    name = character_name()
    character = make_character(name)
    print(make_riddle(character, board))
    player_input = str(get_player_answer())
    correct_riddle_answer = get_correct_answer()
    check_player_answer(player_input, correct_riddle_answer, character)
    print(character)


def main():
    game()


if __name__ == '__main__':
    main()






