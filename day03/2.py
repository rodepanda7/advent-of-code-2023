from math import prod

with open("big-input2.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]

# key are the indices of the left most digit of the number, value is the number
WIDTH = len(grid)
HEIGHT = len(grid[0])

def check_digit(y: int, x: int) -> bool:
    if y < 0 or y >= HEIGHT or x < 0 or x >= WIDTH:
        return False
    
    return grid[y][x].isdigit()

def add_part_number(y: int, x: int) -> tuple[int, int, int]:
    number = ''
    while(check_digit(y, x)):
        x -= 1
    
    x += 1
    x_min = x

    while(check_digit(y, x)):
        number += grid[y][x]
        x += 1
    
    return (x_min, y, int(number))

def get_gear_ratio(y: int, x: int) -> int:
    part_numbers = {}
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            if check_digit(y + i, x + j):
                y_num, x_num, num = add_part_number(y + i, x + j)
                part_numbers[(x_num, y_num)] = num

    if len(part_numbers) != 2:
        return 0
    
    return prod(list(part_numbers.values()))

result = 0
for i, row in enumerate(grid):
    for j, item in enumerate(row):
        if item == '*':
            result += get_gear_ratio(i, j)

print(result)