"""
Name
Student Number
"""
import time
import json
from random import randint


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


def character_name() -> str:
    print("Please enter a name for your character: ")
    return input()


def make_character(name: str) -> dict:
    return {'name': name,
            'level': 1,
            'attempts': 3,
            'XP': 0,
            'x-coordinate': 10,
            'y-coordinate': 1}


def get_user_choice(choices: list) -> int:
    print("Where would you like to go?")
    for number, choice in enumerate(choices, 1):
        print(number, choice)
    player_choice = int(input("Please enter a number to move: "))
    if 1 <= player_choice <= len(choices):
        return player_choice
    else:
        print("That doesn't work! Please try again.")


def validate_move(width: int, height: int, character: dict, direction: int) -> bool:
    if direction == 1 and character['y-coordinate'] < 1:
        return False
    if direction == 2 and character['y-coordinate'] == height:
        return False
    if direction == 3 and character['x-coordinate'] < 1:
        return False
    if direction == 4 and character['x-coordinate'] == width:
        return False
    else:
        return True


def move_character(character: dict, player_movement: int) -> None:
    if player_movement == 1:
        character['y-coordinate'] -= 1
    if player_movement == 2:
        character['y-coordinate'] += 1
    if player_movement == 3:
        character['x-coordinate'] -= 1
    if player_movement == 4:
        character['x-coordinate'] += 1


def game():  # called from main
    rows = 10
    columns = 10
    movements = ['Up', 'Down', 'Left', 'Right']
    board = make_board(rows, columns)
    name = character_name()
    print(f"Welcome to our math game, {name}! We hope you enjoy and practice your math skills. :)")
    time.sleep(2)
    print("Loading...")
    time.sleep(2)
    print("""
    \_/
  --(_)--  .
    / \   /_|
          |-|
    .-----' '-----.                                  __
   /____[SCHOOL]___\                                ()))
    | [] .-.-. [] |                                (((())
  ..|____|_|_|____|..................................)(... 
    """)
    print("You have entered the math academy! We hope you enjoy your time as a student. Be ready to put your thinking cap on!")
    time.sleep(2)
    print("You are now walking inside...")
    time.sleep(1)
    character = make_character(name)
    time.sleep(2)
    print(f"Here are your character stats: {character}")
    time.sleep(2)
    achieved_goal = False
    while not achieved_goal:
        # Tell the user where they are
        # describe_current_location(board, character)
        direction = get_user_choice(movements)
        valid_move = validate_move(rows, columns, character, direction)
        if valid_move:
            move_character(character, direction)
    #         describe_current_location(board, character)
    #         there_is_a_challenge = check_for_challenges()
    #         if there_is_a_challenge:
    #             execute_challenge_protocol(character)
    #             if character_has_leveled():
    #                 execute_glow_up_protocol()
    #     achieved_goal = check_if_goal_attained(board, character)
        else:
            print("Ah! You can't go there. Please try again...")
            print(f"Your current coordinates are {character['x-coordinate'], character['y-coordinate']}")
            time.sleep(2)
    # else:
    #     Tell the user they can't go in that direction
# Print end of game stuff like congratulations or sorry you died


def main():
    game()


if __name__ == '__main__':
    main()
