# describe_current_location -> character's location on the board -> character['coordinates']
# get_user_choice -> show choices, player chooses where they want character to move
# validate_move -> checks if movement is possible on the board
# move_character -> if valid_move is True, move character (character's coordinates change)
# if player chooses move up, character['coordinates'][1]  +1
# if player chooses move down, character['coordinates'][1] -1
# if player chooses move left, character['coordinates'][0] -1
# if player chooses move right, character['coordinates'][0] +1
# describe_current_location -> character's new location -> character['coordinates']

movements = ['Up', 'Down', 'Left', 'Right']


def get_user_choice(choices: list) -> int:
    print("Where would you like to go?")
    for number, choice in enumerate(choices, 1):
        print(number, choice)
    player_choice = int(input("Please enter a number to move: "))
    if 1 <= player_choice <= len(choices):
        return player_choice
    else:
        print("That doesn't work! Please try again.")


# print(get_user_choice(movements))

############


def make_character():
    character_name = input("Please enter a name for your character: ")
    return {'name': character_name,
            'level': 1,
            'attempts': 3,
            'XP': 0,
            'coordinates': (0, 0)}


rows = 10
columns = 10
test_character = make_character()
player_movement = get_user_choice(movements)


def validate_move(width: int, height: int, character: dict, direction: int) -> bool:
    if direction == 1 and character['coordinates'][1] < 1:
        return False
    if direction == 2 and character['coordinates'][1] == height:
        return False
    if direction == 3 and character['coordinates'][0] < 1:
        return False
    if direction == 4 and character['coordinates'][0] == width:
        return False
    else:
        return True


print(validate_move(rows, columns, test_character, player_movement))


def move_character(character):
    if player_movement == 1:
        character['coordinates'] =
    # if player_movement == 2:
    #     character['coordinates'][1] -= 1
    # if player_movement == 3:
    #     character['coordinates'][0] -= 1
    # if player_movement == 4:
    #     character['coordinates'][0] += 1
    # return character


print(move_character(test_character))