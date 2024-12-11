from collections import deque

with open('input.txt') as file:
    data = file.readlines()

grid = [[int(char) for char in line.strip()] for line in data]

trailhead_rating_total = 0
directions = [(-1,0),(1,0),(0,-1),(0,1)]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            queue = deque([(i, j)])
            max_height_positions = set()

            while queue:
                x, y = queue.popleft()
                curr_height = grid[x][y]

                if curr_height == 9:
                    trailhead_rating_total += 1
                    max_height_positions.add((x, y))
                else:
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == curr_height + 1:
                            queue.append((nx, ny))

print(trailhead_rating_total)