with open('input.txt') as file:
    grid, moves = file.read().split("\n\n")

grid = [list(line) for line in grid.split("\n")]
moves = list(filter(lambda x: x != "\n", moves))

curr_pos = (0, 0)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            curr_pos = i, j
            break
    if grid[i][j] == "@":
        grid[i][j] = "."
        break

directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

for move in moves:
    dx, dy = directions[move]
    x, y = curr_pos
    nx, ny = x + dx, y + dy

    if grid[nx][ny] == ".":
        curr_pos = nx, ny
    elif grid[nx][ny] == "O":
        end_x, end_y = nx, ny
        while grid[end_x][end_y] == "O":
            end_x, end_y = end_x + dx, end_y + dy
        
        if grid[end_x][end_y] == ".":
            grid[end_x][end_y] = "O"
            grid[nx][ny] = "."
            curr_pos = nx, ny

total_gps = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "O":
            total_gps += 100 * i + j

print(total_gps)