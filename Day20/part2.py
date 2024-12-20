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
corridor_positions = list(min_distance)
for x1 in range(len(grid)):
    for y1 in range(len(grid[0])):
        for x2 in range(max(0, x1 - 20), min(len(grid), x1 + 21)):
            x_dist = abs(x2 - x1)
            for y2 in range(max(0, y1 - (20 - x_dist)), min(len(grid[0]), y1 + (20 - x_dist) + 1)):
                if (x1, y1) in min_distance and (x2, y2) in min_distance:
                    y_dist = abs(y2 - y1)
                    manhattan_dist = x_dist + y_dist
                    picoseconds_saved = (min_distance[(x2, y2)] - min_distance[(x1, y1)]) - manhattan_dist
                    if picoseconds_saved >= 100:
                        res += 1

print(res)