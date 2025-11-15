with open("big-input1.txt") as f:
    games = [list(map(lambda x: x.strip(), line.split(':')[1].split(';'))) for line in f.read().splitlines()]

games = [[list(map(lambda x: x.strip(), grab.split(','))) for grab in game] for game in games]

RED = 12
GREEN = 13
BLUE = 14

def is_possible_grab(amount: int, color: str) -> bool:
    match color:
        case 'red':
            return amount <= RED
        case 'green':
            return amount <= GREEN
        case 'blue':
            return amount <= BLUE

def is_possible_game(grab: list[list[str]]) -> bool:
    is_possible = True
    for round in grab:
        amount, color = round.split()
        is_possible = is_possible and is_possible_grab(int(amount), color)
    
    return is_possible

result = 0
for i, game in enumerate(games):
    is_possible = True
    for grab in game:
        is_possible = is_possible and is_possible_game(grab)
    if is_possible: 
        result += i + 1
    is_possible = True
print(result)