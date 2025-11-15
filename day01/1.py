with open("big-input1.txt", "r") as file:
    lines = file.read().splitlines()
    
filtered_lines = [list(filter((lambda x: x.isdigit()), list(line))) for line in lines]
result = sum(int(filtered_line[0] + filtered_line[-1]) for filtered_line in filtered_lines)

print(result)