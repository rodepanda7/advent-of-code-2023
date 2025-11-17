with open("big-input2.txt") as f:
    games = [list(map(lambda x: x.strip(), game.split(':')[1].strip().split('|'))) for game in f.readlines()]
    
games = [[set(map(lambda x: x.strip(), deck.split())) for deck in game] for game in games]

NR_CARDS = len(games)

result = 0
# map the index of a card to the number of occurrences of that card
card_dict = {i: 1 for i in range(NR_CARDS)}

def nr_winning_cards(winning_deck: set[int], actual_deck: set[int]) -> int:
    count = 0
    for num in actual_deck:
        if num in winning_deck:
            count += 1

    return count

for i, game in enumerate(games):
    for j in range(1, (nr_winning_cards(game[0], game[1]) + 1)):
        if i + j >= NR_CARDS:
            continue 
        card_dict[i + j] += card_dict[i]

print(f"Result: {sum(card_dict.values())}")