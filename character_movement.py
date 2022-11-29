# describe_current_location -> character's location on the board -> character['coordinates']
# get_user_choice -> show choices, player chooses where they want character to move
# validate_move -> checks if movement is possible on the board
# move_character -> if valid_move is True, move character (character's coordinates change)
# if player chooses move up, character['coordinates'][1]  +1
# if player chooses move down, character['coordinates'][1] -1
# if player chooses move left, character['coordinates'][0] -1
# if player chooses move right, character['coordinates'][0] +1
# describe_current_location -> character's new location -> character['coordinates']

directions = ["Up", "Down", "Left", "Right"]


def get_user_choice(choices):
    print("Where would you like to go?")
    for number, choice in enumerate(choices, 1):
        print(number, choice)
    player_choice = int(input("Please enter a number to move: "))
    if 1 <= player_choice <= len(choices):
        return player_choice
    else:
        print("That doesn't work! Please try again.")


print(get_user_choice(directions))
