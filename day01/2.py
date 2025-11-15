with open("big-input2.txt", "r") as file:
    lines = file.read().splitlines()

number_dict = {"one": 'o1e', "two": 't2o', "three": 't3e', "four": 'f4r', "five": 'f5e', "six": 's6x', "seven": 's7n', "eight": 'e8t', "nine": 'n9e'}

for i, line in enumerate(lines):
    for k in number_dict:
        lines[i] = lines[i].replace(k, number_dict[k])

filtered_lines = [list(filter((lambda x: x.isdigit()), list(line))) for line in lines]
result = sum(int(filtered_line[0] + filtered_line[-1]) for filtered_line in filtered_lines)

print(result)