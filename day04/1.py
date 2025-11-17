with open("big-input1.txt") as f:
    games = [list(map(lambda x: x.strip(), game.split(':')[1].strip().split('|'))) for game in f.readlines()]
    
games = [[set(map(lambda x: x.strip(), deck.split())) for deck in game] for game in games]

result = 0

for game in games:
    count = 0
    for card in game[1]:
        if card in game[0]:
            count += 1
    
    if count > 0:
        result += 2**(count-1)

print(result)