with open('input-example.txt') as file:
    data = file.readlines()

grid = [list(line.strip()) for line in data]

start_x, start_y = 0, 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "^":
            start_x, start_y = i, j
            grid[i][j] = "."
            break
    if grid[i][j] == "^":
        break

directions = [(-1,0),(0,1),(1,0),(0,-1)]
loop_causing_positions = 0

def get_move(x, y, directions_index):
    dx, dy = directions[directions_index]
    nx, ny = x + dx, y + dy

    if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) or grid[nx][ny] != "#":
        return nx, ny, directions_index
    else:
        directions_index = (directions_index + 1) % len(directions)
        return x, y, directions_index

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "." and not (i == start_x and j == start_y):
            grid[i][j] = "#"
        
            x, y = start_x, start_y

            slow_x, slow_y, slow_directions_index = start_x, start_y, 0
            fast_x, fast_y, fast_directions_index  = get_move(slow_x, slow_y, slow_directions_index)

            while (0 <= fast_x < len(grid) and 0 <= fast_y < len(grid[0])) and not (slow_x == fast_x and slow_y == fast_y and slow_directions_index == fast_directions_index):
                slow_x, slow_y, slow_directions_index = get_move(slow_x, slow_y, slow_directions_index)
                fast_x, fast_y, fast_directions_index = get_move(fast_x, fast_y, fast_directions_index)
                fast_x, fast_y, fast_directions_index = get_move(fast_x, fast_y, fast_directions_index)
            
            if slow_x == fast_x and slow_y == fast_y and slow_directions_index == fast_directions_index:
                loop_causing_positions += 1
            
            grid[i][j] = "."

print(loop_causing_positions)