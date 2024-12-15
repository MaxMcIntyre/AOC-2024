from collections import deque

with open('input.txt') as file:
    grid_data, moves = file.read().split("\n\n")

moves = list(filter(lambda x: x != "\n", moves))

grid = []
grid_row = []
for i in range(len(grid_data)):
    if grid_data[i] == "." or grid_data[i] == "#":
        grid_row.extend([grid_data[i]] * 2)
    elif grid_data[i] == "@":
        grid_row.append("@")
        grid_row.append(".")
    elif grid_data[i] == "O":
        grid_row.append("[")
        grid_row.append("]")
    elif grid_data[i] == "\n":
        grid.append(grid_row.copy())
        grid_row = []
grid.append(grid_row.copy())

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

def handle_adjacent(x, y, queue, box_types):
    if grid[x][y] == "[":
        queue.append((x, y + 1))
        box_types[(x, y + 1)] = grid[x][y + 1]
    else:
        queue.append((x, y - 1))
        box_types[(x, y - 1)] = grid[x][y - 1] 

for move in moves:
    dx, dy = directions[move]
    x, y = curr_pos
    nx, ny = x + dx, y + dy

    if grid[nx][ny] == ".":
        curr_pos = nx, ny
    elif grid[nx][ny] in ["[", "]"]:
        queue = deque([(nx, ny)])
        box_types = {(nx, ny): grid[nx][ny]}
        handle_adjacent(nx, ny, queue, box_types)
        
        can_move = True
        while queue:
            x, y = queue.popleft()
            bx, by = x + dx, y + dy
            if grid[bx][by] == "#":
                can_move = False
                break
            elif grid[bx][by] in ["[", "]"] and (bx, by) not in box_types:
                queue.append((bx, by))
                box_types[(bx, by)] = grid[bx][by]
                handle_adjacent(bx, by, queue, box_types)
        
        if can_move:
            new_box_positions = set()
            for (x, y), cell_type in box_types.items():
                bx, by = x + dx, y + dy
                new_box_positions.add((bx, by))
                grid[bx][by] = cell_type
            for (x, y) in box_types:
                if (x, y) not in new_box_positions:
                    grid[x][y] = "."

            curr_pos = nx, ny

total_gps = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "[":
            total_gps += 100 * i + j

print(total_gps)