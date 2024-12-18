from part1 import find_path

with open('input.txt') as file:
    positions = list(map(lambda x: tuple(map(int, x.split(','))), file.read().split("\n")))

grid = [["." for _ in range(71)] for _ in range(71)]

for i in range(1024):
    pos_x, pos_y = positions[i]
    grid[pos_x][pos_y] = "#"

i = 1023
first_block_byte = (0, 0)

while i < len(positions):
    path = find_path(grid)
    if not len(path) - 1:
        first_block_byte = positions[i]
        break

    while i < len(positions):
        i += 1
        pos_x, pos_y = positions[i]
        grid[pos_x][pos_y] = "#"
        if (pos_x, pos_y) in path:
            break

print(first_block_byte)