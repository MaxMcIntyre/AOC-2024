from collections import defaultdict

with open('input.txt') as file:
    data = file.readlines()

grid = [list(line.strip()) for line in data]

node_locations = defaultdict(list)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != ".":
            node_locations[grid[i][j]].append((i, j))

antinode_locations = set()

for type in node_locations:
    for i in range(len(node_locations[type])):
        x_1, y_1 = node_locations[type][i]
        for j in range(i+1, len(node_locations[type])):
            x_2, y_2 = node_locations[type][j]
            dx, dy = x_2 - x_1, y_2 - y_1
            possible_antinodes = [(x_1 - dx, y_1 - dy), (x_2 + dx, y_2 + dy)]
            for x_a, y_a in possible_antinodes:
                if 0 <= x_a < len(grid) and 0 <= y_a < len(grid[0]):
                    antinode_locations.add((x_a, y_a))

print(len(antinode_locations))