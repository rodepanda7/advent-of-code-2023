with open("big-input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    seeds = [int(seed) for seed in lines[0].split(":")[1].strip().split()]

maps = []
i = -1
for line in lines[1:]:
    if line == "":
        i += 1
        maps.append([])
    try:
        dest, source, range = [int(num) for num in line.split()]
        maps[i].append({"dest": dest, "source": source, "range": range})
    except Exception:
        pass

def map_seed(iteration: int, seed: int) -> int:
    for rule in maps[iteration]:
        if seed >= rule["source"] and seed <= rule["source"] + rule["range"]:
            return seed + (rule["dest"] - rule["source"])
    return seed

def get_location_number(seed: int) -> int:
    for i, map in enumerate(maps):
        seed = map_seed(i, seed)
    return seed

location_nums = []
for seed in seeds:
    location_nums.append(get_location_number(seed))
print(min(location_nums))