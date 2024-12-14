import re

with open('input.txt') as file:
    entries = file.read().split("\n")

quadrants = [0,0,0,0]

pos_vels = []
for entry in entries:
    vals = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", entry)
    pos_vel = int(vals.group(1)), int(vals.group(2)), int(vals.group(3)), int(vals.group(4))
    pos_vels.append(pos_vel)

grid = [["." for _ in range(103)] for _ in range(101)]

seconds = 1
while True:
    for i in range(len(pos_vels)):
        pos_x, pos_y, vel_x, vel_y = pos_vels[i]
        grid[pos_x][pos_y] = "."
        pos_x, pos_y = (pos_x + vel_x) % 101, (pos_y + vel_y) % 103
        grid[pos_x][pos_y] = "#"
        pos_vels[i] = (pos_x, pos_y, vel_x, vel_y)

    max_consecutive_robots = 0
    for i in range(len(grid)):
        consecutive_robots = 0
        for j in range(len(grid)):
            if grid[i][j] == "#":
                consecutive_robots += 1
                max_consecutive_robots = max(max_consecutive_robots, consecutive_robots)
            else:
                consecutive_robots = 0
    
    if max_consecutive_robots >= 20:
        break
    
    seconds += 1

print(seconds)