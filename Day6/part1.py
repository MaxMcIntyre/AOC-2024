with open('input.txt') as file:
    data = file.readlines()

grid = [list(line.strip()) for line in data]

x, y = 0, 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "^":
            x, y = i, j
            grid[i][j] = "."
            break
    if grid[i][j] == "^":
        break

directions = [(-1,0),(0,1),(1,0),(0,-1)]
directions_index = 0
positions_reached = 0

while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
    if grid[x][y] == ".":
        positions_reached += 1
        grid[x][y] = "X"

    dx, dy = directions[directions_index]
    nx, ny = x + dx, y + dy
    if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) or grid[nx][ny] != "#":
        x, y = nx, ny
    else:
        directions_index = (directions_index + 1) % len(directions)

print(positions_reached)