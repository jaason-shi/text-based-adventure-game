"""
Name
Student Number
"""
import time
import json
from random import randint
from board import make_board, print_board
from movement import get_user_choice, validate_move, move_character
from check_answers import get_player_answer, get_correct_answer, check_player_answer, \
    get_player_final_answer, check_player_final_answer
from ascii_art import school_art, grad_cap, teacher


def character_name() -> str:
    """
    Return user input.

    :postcondition: prints the user input
    :return: the user input as a string
    """
    print("Please enter a name for your character: ")
    return input()


def make_character(name: str) -> dict:
    """
    Return a dictionary representing the character information.

    :param name: a string
    :precondition: name must be a string
    :postcondition: creates a dictionary with the player's name and their character stats
    :postcondition: name does not change
    :return: a dictionary with the character stats

    >>> make_character('chris')
    {'Name': 'chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 5, 'y-coordinate': 5}
    """
    return {'Name': name,
            'Grade': 1,
            'Attempts': 3,
            'XP': 0,
            'x-coordinate': 5,
            'y-coordinate': 5}


def check_for_room(character: dict, board: dict) -> bool:
    """
    Determine if the character's current room is not hallway.

    :param character: a dictionary
    :param board: a dictionary
    :precondition: character must be a dictionary with the character attribute keys of 'x-coordinate' and 'y-coordinate'
    :precondition: board must be a dictionary representing the current game board
    :postcondition: correctly determines if the character's current room is not hallway
    :postcondition: character and board are unchanged
    :return: True if character's current room is not hallway, else False

    >>> test_character = {'Name': 'chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 0, 'y-coordinate': 0}
    >>> test_board = {(0, 0): 'hallway', (0, 1): 'art room'}
    >>> check_for_room(test_character, test_board)
    False
    >>> test_character_two = {'Name': 'chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 0, 'y-coordinate': 1}
    >>> check_for_room(test_character_two, test_board)
    True
    """
    current_character_coordinate = (character['x-coordinate'], character['y-coordinate'])
    current_room = board[current_character_coordinate]
    if current_room != 'hallway':
        return True
    else:
        return False


def make_riddle(riddle_number: int) -> str:
    """
    Return the value as a string from the dictionary key "riddles" by using the riddle_number as the index.

    :param riddle_number: an integer
    :precondition: riddle_number must be an integer from [0, 12]
    :postcondition: correctly returns value as a string from dictionary key "riddles"
    :postcondition: riddle_number is unchanged
    :return: a string from the dictionary key "riddles" by using the riddle_number as the index

    >>> make_riddle(0)
    'There are several books on a bookshelf. If one book is the 4th from the left and 6th from the right, how many books are on the shelf?'
    """
    get_riddles = open('riddles.json', 'r')
    riddles = json.load(get_riddles)
    return riddles['riddles_list'][riddle_number]["riddles"]


def player_is_correct(character: dict) -> None:
    """
    Character will gain XP and lose an attempt.

    Character will gain XP, attempts, grades if character has reached a certain value of XP.

    :param character: a dictionary
    :precondition: character must be a dictionary with the character attribute keys of 'XP', 'Attempts' and 'Grades'
    :postcondition: correctly decrements value of character attempts by 1, increments value of character xp by 10
    :postcondition: correctly increments value of character grade by 1, attempts by 3 if character xp has reached 10
    :postcondition: correctly increments value of character grade by 1, attempts by 3 if character xp has reached 30
    """
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
        time.sleep(1)
        print("Ominous boss music begins to play... the principal appears in front of you")


def player_is_wrong(character: dict) -> None:
    """
    Character will lose an attempt and receive a print message.

    :param character: a dictionary
    :precondition: character must be a dictionary with the character attribute key of 'Attempts'
    :postcondition: correctly decrements value of character attempts by 1
    """
    print("Oh no, that is not correct. You have some reviewing to do.")
    character['Attempts'] -= 1
    print(character)


def no_more_attempts(character: dict) -> bool:
    """
    Determine if the value of attempts is 0 from the character.

    :param character: a dictionary
    :precondition: character must be a dictionary with the character attribute key of 'Attempts'
    :postcondition: correctly determines if value of character attempts is 0
    :postcondition: character is unchanged
    :return: True if character attempts is 0, else False

    >>> test_character = {'Name': 'chris', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 0, 'y-coordinate': 0}
    >>> no_more_attempts(test_character)
    False
    >>> test_character_two = {'Name': 'chris', 'Grade': 1, 'Attempts': 0, 'XP': 0, 'x-coordinate': 0, 'y-coordinate': 0}
    >>> no_more_attempts(test_character_two)
    True
    """
    if character['Attempts'] == 0:
        print('You dropped out of the academy. :( Please reapply next year...')
        return True


def check_if_goal_attained(character: dict) -> bool:
    """
    Determine if the goal of Grade 3 is attained from the character.

    :param character: dictionary
    :precondition: character must be a dictionary with the character attribute key of 'Grade'
    :postcondition: correctly determines if value character grade is attained
    :postcondition: character is unchanged
    :return: True if character grade is 3, else False
    """
    if character['Grade'] == 3:
        return True


def game():
    """
    Run the game.

    """
    rows = 10
    columns = 10
    movements = ['Up', 'Down', 'Left', 'Right']
    board = make_board(rows, columns)
    name = character_name().title()
    print(f"Welcome to Akademia Matematyczna, {name}! "
          f"You have been accepted into our intense program. Only select few are enrolled at our academy :)")
    time.sleep(1)
    print("Loading...")
    time.sleep(1.5)
    school_art()
    print("You have entered the math academy! Walk around to explore the school grounds.")
    print("POP QUIZZES are scattered in some of the rooms so be ready to put your thinking cap on! "
          "These are mandatory and closed book quizzes... ")
    print("To graduate from the academy, you will need to do these quizzes to reach Grade 3 and take the final exam. "
          "No cheating allowed!")
    time.sleep(1)
    print("You are now walking inside...")
    time.sleep(1)
    character = make_character(name)
    time.sleep(1)
    print(f"Here are your character stats: {character}")
    time.sleep(1)
    achieved_goal = False
    while not achieved_goal:
        print_board(board, rows, columns, character)
        time.sleep(2)
        direction = get_user_choice(movements)
        valid_move = validate_move(rows, columns, character, direction)

        if valid_move:
            move_character(character, direction)
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

            if no_more_attempts(character):
                achieved_goal = True

            # if character level == 3
            if check_if_goal_attained(character):
                time.sleep(2)
                teacher()
                print('You made it to Grade 3! 🤓 It is time for the final exam... be prepared! 📚'
                      'This is mandatory and closed book. I will find you if you cheat...')
                time.sleep(2)
                print('Final Exam: Seven boys met each other at a party. '
                      'Each of them shook hands only once with each of the other boys. '
                      'What is the total number of handshakes that took place?')
                final_player_answer = get_player_final_answer()
                correct_player_final_answer = check_player_final_answer(final_player_answer)

                if correct_player_final_answer:
                    achieved_goal = True
                    print("Congratulations! You have graduated from the academy.")
                    grad_cap()
                else:
                    character['Grade'] -= 1
                    print("Oh no, you need to go review Grade 2 again...")
                    print(f"Here are your character stats: {character}")

        else:
            print("Ah! You can't go there. Please try again...")
            print(f"Your current coordinates are {character['x-coordinate'], character['y-coordinate']}")
            time.sleep(2)


def main():
    """
    Drive the program.

    """
    game()


if __name__ == '__main__':
    main()
