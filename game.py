"""
Name
Student Number
"""
import time
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
    :postcondition: rows and columns are unchanged
    :return: a dictionary that has hallways and rooms from a JSON file for every tile in the game
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
    """
    return {'Name': name,
            'Grade': 1,
            'Attempts': 3,
            'XP': 0,
            'x-coordinate': 5,
            'y-coordinate': 5}


def describe_current_location(board: dict, character: dict) -> str:
    character_coordinate = (character['x-coordinate'], character['y-coordinate'])
    character_location_on_board = board[character_coordinate]['room']
    return f"Your current location is: {character_location_on_board}"


def get_user_choice(choices: list) -> int:
    """
    Return the player's inputted choice.

    :param choices: a list
    :precondition: choices must be a list of possible options for a player to choose from
    :postcondition: correctly returns an integer that represents the player's choice
    :postcondition: the choices list is unchanged
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


def validate_move(width: int, height: int, character: dict, direction: int) -> bool:
    """
    Return True if character's move is valid on the game board based on the board size, False otherwise.

    :param width: an integer
    :param height: an integer
    :param character: a dictionary
    :param direction: an integer
    :precondition: width must be a positive non-zero integer
    :precondition: height must be a positive non-zero integer
    :precondition: character must be a dictionary with the attribute keys of 'x-coordinate' and 'y-coordinate'
    :precondition: direction must be an integer representing the movement that the user input (1, 2, 3, or 4)
    :postcondition: return True if character's coordinate and user's next movement are within the board coordinates
    :postcondition: return False if character's coordinate and user's next movement are not in the board coordinates
    :return: True or False
    """
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
    """
    Update character dictionary with new 'x-coordinate' and 'y-coordinate' values based on the player's movement.

    :param character: a dictionary
    :param player_movement: an integer
    :precondition: character must be a dictionary with the attribute keys of 'x-coordinate' and 'y-coordinate'
    :precondition: player_movement must be an integer representing the movement that the user input (1, 2, 3, or 4)
    :postcondition: correctly changes character dictionary values of the 'x-coordinate' and 'y-coordinate' keys
    :postcondition: player_movement is unchanged
    """
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
    current_room = board[current_character_coordinate]
    if current_room != 'hallway':
        return True
    else:
        return False


def make_riddle(riddle_number: int) -> str:
    get_riddles = open('riddles.json', 'r')
    riddles = json.load(get_riddles)
    return riddles['riddles_list'][riddle_number]["riddles"]


def get_player_answer() -> str:
    """
    Return user input.

    :postcondition: prints the user input
    :return: the user input as a string
    """
    print("Please enter your answer here: ")
    return input()


def get_correct_answer(riddle_number: int) -> str:
    """
    Return the value as a string from dictionary key "answer" by using the riddle_number as the index.

    :param riddle_number: an integer
    :precondition: riddle_number must be an integer from [0, 12]
    :postcondition: correctly returns value as a string from dictionary key "answer"
    :postcondition: riddle_number is unchanged
    :return: a string from the dictionary key "answer" by using the riddle_number as the index
    """
    get_riddles = open('riddles.json', 'r')
    riddles = json.load(get_riddles)
    correct_answer = riddles['riddles_list'][riddle_number]["answer"]
    return correct_answer


def check_player_answer(player_answer: str, correct_answer: str) -> bool:
    """
    Determine if the player answer is the same as the correct answer.

    :param player_answer: a string
    :param correct_answer: a string
    :precondition: player_answer must be a string
    :precondition: correct_answer must be a string
    :postcondition: correctly determines if player_answer is same as correct_answer
    :postcondition: player_answer and correct_answer are unchanged
    :return: True if player_answer is same as correct_answer, else False
    """
    if player_answer == correct_answer:
        return True
    else:
        return False


def get_player_final_answer() -> str:
    """
    Return user input.

    :postcondition: prints the user input
    :return: the user input as a string
    """
    print("Please enter your final answer here: ")
    return input()


def check_player_final_answer(final_player_answer: str) -> bool:
    """
    Determine if the final player answer is the value 21.

    :param final_player_answer: a string
    :precondition: final_player_answer must be a string
    :postcondition: correctly determines if final_player_answer is 21
    :postcondition: final_player_answer is unchanged
    :return: True if final_player_answer is the value of 21, else False
    """
    if final_player_answer == '21':
        return True
    else:
        return False


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
        print('You made it to Grade 3! It is time for the final exam... be prepared!')


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
    print(f"Welcome to the math academy, {name}! We hope to see you graduate with flying colours! :)")
    time.sleep(1)
    print("Loading...")
    time.sleep(1.5)
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
        # print(describe_current_location(board, character))
        print_board(board, rows, columns, character)
        time.sleep(2)
        direction = get_user_choice(movements)
        valid_move = validate_move(rows, columns, character, direction)

        if valid_move:
            move_character(character, direction)
            # print(describe_current_location(board, character))

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
                print('Seven boys met each other at a party. '
                      'Each of them shook hands only once with each of the other boys. '
                      'What is the total number of handshakes that took place?')
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


def main():
    """
    Drive the program.

    """
    game()


if __name__ == '__main__':
    main()
