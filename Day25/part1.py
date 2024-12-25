with open('input.txt') as file:
    data = file.read().split("\n\n")

locks = []
keys = []

for grid in data:
    rows = grid.split("\n")

    if rows[0] == "#####":
        locks.append(rows)
    elif rows[-1] == "#####":
        keys.append(rows)

def calculate_heights(schematic):
    heights = []
    for i in range(len(schematic[0])):
        height = 0
        for j in range(len(schematic)):
            if schematic[j][i] == "#":
                height += 1
        heights.append(height - 1)
    return heights

correct_combinations = 0
for lock in locks:
    lock_heights = calculate_heights(lock)
    for key in keys:
        key_heights = calculate_heights(key)
        if all(key_heights[i] + lock_heights[i] <= 5 for i in range(len(lock_heights))):
            correct_combinations += 1

print(correct_combinations)