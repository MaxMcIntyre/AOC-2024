import heapq

with open('input.txt') as file:
    grid = [list(line.strip()) for line in file.readlines()]

start_pos = (0, 0)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start_pos = i, j
            break
    if grid[i][j] == "S":
        grid[i][j] = "."
        break

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
pq = [(0, (start_pos[0], start_pos[1], 1))]
visited = set()
optimal_cost = float('inf')

while pq:
    cost, curr = heapq.heappop(pq)
    x, y, direction = curr
    if curr in visited:
        continue
    visited.add(curr)

    if grid[x][y] == "E":
        optimal_cost = cost
        break

    dx, dy = directions[direction]
    nx, ny = x + dx, y + dy
    if grid[nx][ny] != "#":
        heapq.heappush(pq, (cost + 1, (nx, ny, direction)))
    
    direction_r = (direction + 1) % len(directions)
    dx_r, dy_r = directions[direction_r]
    if grid[x + dx_r][y + dy_r] != "#":
        heapq.heappush(pq, (cost + 1000, (x, y, direction_r)))
    
    direction_l = (direction - 1) % len(directions)
    dx_l, dy_l = directions[direction_l]
    if grid[x + dx_l][y + dy_l] != "#":
        heapq.heappush(pq, (cost + 1000, (x, y, direction_l)))

print(optimal_cost)