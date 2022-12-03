import json


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
