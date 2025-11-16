with open("big-input1.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]

# key are the indices of the left most digit of the number, value is the number
part_numbers = {}
WIDTH = len(grid)
HEIGHT = len(grid[0])

def check_digit(y: int, x: int) -> bool:
    if y < 0 or y >= HEIGHT or x < 0 or x >= WIDTH:
        return False
    
    return grid[y][x].isdigit()

def add_part_number(y: int, x: int) -> int:
    number = ''
    while(check_digit(y, x)):
        x -= 1
    
    x += 1
    x_min = x

    while(check_digit(y, x)):
        number += grid[y][x]
        x += 1
    
    part_numbers[(x_min, y)] = int(number)

def add_all_part_numbers(y: int, x: int) -> None:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            if check_digit(y + i, x + j):
                add_part_number(y + i, x + j)

for i, row in enumerate(grid):
    for j, item in enumerate(row):
        if item != '.' and not item.isdigit():
            add_all_part_numbers(i, j)

print(sum(n for n in part_numbers.values()))