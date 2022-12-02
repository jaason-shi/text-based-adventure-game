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
    """
    Return user input.

    :return:
    """
    print("Please enter a name for your character: ")
    return input()


def make_character(name: str) -> dict:
    return {'Name': name,
            'Grade': 1,
            'Attempts': 3,
            'XP': 0,
            'x-coordinate': 9,
            'y-coordinate': 1}


def describe_current_location(board: dict, character: dict) -> str:
    character_coordinate = character['x-coordinate'], character['y-coordinate']
    character_location_on_board = board[character_coordinate]['room']
    return f"Your current location is: {character_location_on_board}"


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
    if direction == 2 and character['y-coordinate'] == height - 1:
        return False
    if direction == 3 and character['x-coordinate'] < 1:
        return False
    if direction == 4 and character['x-coordinate'] == width - 1:
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


def check_for_room(character: dict, board: dict) -> bool:
    current_character_coordinate = (character['x-coordinate'], character['y-coordinate'])
    current_room = board[current_character_coordinate]['room']
    if current_room != 'hallway':
        return True
    else:
        return False


def make_riddle(riddle_number: int) -> str:
    get_riddles = open('riddles.json', 'r')
    riddles = json.load(get_riddles)
    return riddles['riddles_list'][riddle_number]["riddles"]


def get_player_answer() -> str:
    print("Please enter your answer here: ")
    return input()


def get_correct_answer(riddle_number: int) -> str:
    get_riddles = open('riddles.json', 'r')
    riddles = json.load(get_riddles)
    correct_answer = riddles['riddles_list'][riddle_number]["answer"]
    return correct_answer


def check_player_answer(player_answer: str, correct_answer: str) -> bool:
    if player_answer == correct_answer:
        return True
    else:
        return False


def make_final_riddle() -> str:
    final_riddle = 'Seven boys met each other at a party. ' \
                   'Each of them shook hands only once with each of the other boys. ' \
                   'What is the total number of handshakes that took place?'
    return final_riddle


def get_player_final_answer() -> str:
    print("Please enter your final answer here: ")
    return input()


def check_player_final_answer(final_player_answer: str) -> bool:
    if final_player_answer == '21':
        return True
    else:
        return False


def player_is_correct(character: dict) -> None:
    print("Correct! You have gained 10 XP")
    character['XP'] += 10
    character['Attempts'] -= 1
    if character['XP'] == 10:
        character["Grade"] += 1
        character["Attempts"] += 3
        print('You made it to Grade 2!')
    elif character['XP'] == 30:
        character["Grade"] += 1
        character["Attempts"] += 3
        print('You made it to Grade 3! It is time for the final exam... be prepared!')


def player_is_wrong(character: dict) -> None:
    print("Oh no, that is not correct. You have some reviewing to do.")
    character['Attempts'] -= 1
    print(character)


def no_more_attempts(character: dict) -> bool:
    if character['Attempts'] == 0:
        print('You dropped out of the academy. :( Please reapply next year...')
    return True


def check_if_goal_attained(character: dict) -> bool:
    if character['Grade'] == 3:
        return True


def game():  # called from main
    rows = 10
    columns = 10
    movements = ['Up', 'Down', 'Left', 'Right']
    board = make_board(rows, columns)
    name = character_name().title()
    print(f"Welcome to the math academy, {name}! We hope to see you graduate with flying colours! :)")
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
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
    print("You have entered the math academy! Walk around to explore the school grounds. "
          "There may be a POP QUIZ in some of the rooms so be ready to put your thinking cap on!")
    time.sleep(1)
    print("You are now walking inside...")
    time.sleep(1)
    character = make_character(name)
    time.sleep(1)
    print(f"Here are your character stats: {character}")
    time.sleep(1)
    achieved_goal = False
    while not achieved_goal:
        # Tell the user where they are
        print(describe_current_location(board, character))
        direction = get_user_choice(movements)
        valid_move = validate_move(rows, columns, character, direction)

        if valid_move:
            move_character(character, direction)
            print(describe_current_location(board, character))

    #         there_is_a_challenge = check_for_challenges()
    #         if there_is_a_challenge:
            print(character)

            there_is_a_room = check_for_room(character, board)
            if there_is_a_room:
                riddle_number = randint(0, 12)
                print(make_riddle(riddle_number))
                player_answer = get_player_answer()
                correct_answer = get_correct_answer(riddle_number)
                if check_player_answer(player_answer, correct_answer):
                    player_is_correct(character)
                    print(character)
                else:
                    player_is_wrong(character)
                    # zero_attempts_left = no_more_attempts(character)
                    # if zero_attempts_left:
                    #     achieved_goal = True


            # if character level == 3
            if check_if_goal_attained(character):
                print(make_final_riddle())
                final_player_answer = get_player_final_answer()
                correct_player_final_answer = check_player_final_answer(final_player_answer)

                if correct_player_final_answer:
                    achieved_goal = True
                    print("Congratulations! You have graduated from the academy.")
                else:
                    character['Grade'] -= 1
                    print("Oh no, you need to go review Grade 2 again...")
                    print(f"Here are your character stats: {character}")

        else:
            print("Ah! You can't go there. Please try again...")
            print(f"Your current coordinates are {character['x-coordinate'], character['y-coordinate']}")
            time.sleep(2)

# Print end of game stuff like congratulations or sorry you died


def main():
    game()


if __name__ == '__main__':
    main()
