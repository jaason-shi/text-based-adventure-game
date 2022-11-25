def make_character():
    character_name = input("Please enter a name for your character: ")
    level = 1
    attempts = 3
    experience_points = 0
    return {'name': character_name, 'level': level, 'attempts': attempts, 'XP': experience_points}


print(make_character())
