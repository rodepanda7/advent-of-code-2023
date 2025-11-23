with open("big-input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    seeds = lines[0].split(":")[1].strip().split()
    seeds = [(int(seeds[i]), int(seeds[i+1])) for i in range(0, len(seeds) - 1, 2)]

maps = []
i = -1
for line in lines[1:]:
    if line == "":
        i += 1
        maps.append([])
    try:
        dest, source, length = [int(num) for num in line.split()]
        maps[i].append({"dest": dest, "source": source, "length": length})
    except Exception:
        pass

# Returns remaining seed ranges that couldn't be mapped
# If a rule can be applied, update mapped_seed_ranges and return the remaining seed ranges that couldn't be mapped
def map_seed_range_rule(seed: int, length: int, dest: int, start: int, l: int, mapped_seed_ranges) -> list[tuple[int, int]]:
    if seed + length < start:
        return [(seed, length)]
    
    if start + l < seed:
        return [(seed, length)]
    
    diff = dest - start
    if seed >= start:
        if seed + length <= start + l:
            mapped_seed_ranges.append((seed + diff, length))
            return []
        else:
            mapped_seed_ranges.append((seed + diff, start + l - seed))
            length = length - (start + l - seed)
            seed = start + l
            return [(seed, length)]

    if seed < start:
        if seed + length <= start + l:
            mapped_seed_ranges.append((start + diff, seed + length - start))
            length = start - seed
            return [(seed, length)]
        else:
            mapped_seed_ranges.append((start + diff, l))
            return [(seed, start - seed), (start + l, seed + length - (start + l))]
    
    return [(seed, length)]

# Applies all rules to a seed range and returns the remaining seed ranges that couldn't be mapped
def map_seed_range_rules(rules: list[dict[str, int]], seed: int, length: int) -> list[tuple[int, int]]:
    mapped_seed_ranges = []
    seed_ranges = [(seed, length)]
    for rule in rules:
        dest, start, l = rule["dest"], rule["source"], rule["length"]
        new_seed_ranges = []
        for seed_range in seed_ranges:
            seed, length = seed_range
            new_seed_ranges.extend(map_seed_range_rule(seed, length, dest, start, l, mapped_seed_ranges))
        seed_ranges = new_seed_ranges

    mapped_seed_ranges.extend(seed_ranges)

    return mapped_seed_ranges

# Maps a seed range through all maps and returns the lowest mapped seed
def map_seed_range(seed_range: tuple[int, int]) -> int:
    seed_ranges = [seed_range]
    new_seed_ranges = [seed_range]
    for i in range(len(maps)):
        seed_ranges = new_seed_ranges
        new_seed_ranges = []
        for seed_range in seed_ranges:
            new_seed_ranges.extend(map_seed_range_rules(maps[i], seed_range[0], seed_range[1]))

    return min(new_seed_ranges, key=lambda t: t[0])[0]

lowest_seeds = []
for i in range(len(seeds)):
    lowest_seeds.append(map_seed_range(seeds[i]))

print(min(lowest_seeds))