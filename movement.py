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
    :precondition: direction must be an integer representing the movement that the user input that is [1, 2, 3, 4]
    :postcondition: return True if character's coordinate and user's next movement are within the board coordinates
    :postcondition: return False if character's coordinate and user's next movement are not in the board coordinates
    :postcondition: width and height are unchanged
    :postcondition: character is unchanged
    :postcondition: direction is unchanged
    :return: True or False

    >>> test_character = {'Name': 'Test', 'Grade': 1, 'Attempts': 3, 'XP': 0, 'x-coordinate': 5, 'y-coordinate': 0}
    >>> validate_move(10, 10, test_character, 1)
    False
    >>> validate_move(10, 10, test_character, 2)
    True
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
    :precondition: player_movement must be an integer representing the movement that the user input that is [1, 2, 3, 4]
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
