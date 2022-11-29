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
    while True:
        print("Where would you like to go?")
        for number, choice in enumerate(choices, 1):
            print(number, choice)
        player_choice = int(input("Please enter a number to move: "))
        if 1 <= player_choice <= len(choices):
            return player_choice
        else:
            print("That doesn't work! Please try again.")
        return


# print(get_user_choice(movements))

############


def make_board(rows, columns):
    board_dict = {}
    for row in range(rows):
        for column in range(columns):
            board_dict[(row, column)] = "x"
    return board_dict


test_rows = 10
test_columns = 10
board = make_board(test_rows, test_columns)


def character_name() -> str:
    print("Please enter a name for your character: ")
    return input()


def make_character(name):
    return {'name': name,
            'level': 1,
            'attempts': 3,
            'XP': 0,
            'x-coordinate': 10,
            'y-coordinate': 10}


print(make_character(character_name()))


test_character = make_character('nat')
player_movement = get_user_choice(movements)


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


print(validate_move(test_rows, test_columns, test_character, player_movement))


def move_character(direction, board_param, character):
    if player_movement == 1:
        character['y-coordinate'] += 1
    if player_movement == 2:
        character['y-coordinate'] -= 1
    if player_movement == 3:
        character['x-coordinate'] -= 1
    if player_movement == 4:
        character['x-coordinate'] += 1
    return character


print(move_character(1, board, test_character))



