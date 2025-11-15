with open("small-input2.txt", "r") as f:
    lines = [list(map(lambda x: x.strip(), line.split(':')[1].split(';'))) for line in f.readlines()]

games = [[list(map(lambda x: x.strip(), grab.split(','))) for grab in game] for game in lines]

RED = 12
GREEN = 13
BLUE = 14

def get_nr_balls(grab: list[str]) -> tuple[int, int, int]:
    red, green, blue = 0, 0, 0
    for round in grab:
        amount, color = round.split()
        match color:
            case 'red':
                red = int(amount)
            case 'green':
                green = int(amount)
            case 'blue':
                blue = int(amount)
    
    return red, green, blue

def get_nr_balls_game(game: list[list[str]]) -> tuple[int, int, int]:
    red, green, blue = 0, 0, 0
    for grab in game:
        new_red, new_blue, new_green = get_nr_balls(grab)
        red, green, blue = max(red, new_red), max(green, new_green), max(blue, new_blue),

    return red, green, blue

result = 0
for game in games:
    red, green, blue = get_nr_balls_game(game)
    result += red * green * blue

print(result)