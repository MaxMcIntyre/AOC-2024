from collections import deque

with open('input.txt') as file:
    grid = [list(line.strip()) for line in file.readlines()]

start_pos = (0, 0)
end_pos = (0, 0)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start_pos = i, j
        elif grid[i][j] == "E":
            end_pos = i, j

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
queue = deque([(end_pos, 0)])
visited = set([end_pos])
min_distance = dict()

while queue:
    curr, dist = queue.popleft()
    min_distance[curr] = dist
    x, y = curr

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#" and (nx, ny) not in visited:
            queue.append(((nx, ny), dist + 1))
            visited.add((nx, ny))

res = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] != "#":
            for dx, dy in directions:
                nx_wall, ny_wall = x + dx, y + dy
                nx_corridor, ny_corridor = x + 2 * dx, y + 2 * dy
                if 0 <= nx_corridor < len(grid) and 0 <= ny_corridor < len(grid[0]) and grid[nx_wall][ny_wall] == "#" and grid[nx_corridor][ny_corridor] != "#":
                    picoseconds_saved = (min_distance[(nx_corridor, ny_corridor)] - min_distance[(x, y)]) - 2
                    if picoseconds_saved >= 100:
                        res += 1

print(res)