import re
from functools import reduce
import operator

with open('input.txt') as file:
    entries = file.read().split("\n")

quadrants = [0,0,0,0]

for entry in entries:
    vals = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", entry)
    pos_x, pos_y, vel_x, vel_y = int(vals.group(1)), int(vals.group(2)), int(vals.group(3)), int(vals.group(4))
    print(pos_x, pos_y, vel_x, vel_y)

    for i in range(100):
        pos_x, pos_y = (pos_x + vel_x) % 101, (pos_y + vel_y) % 103
    
    midpoint_x = 101 // 2
    midpoint_y = 103 // 2
    if pos_x < midpoint_x:
        if pos_y < midpoint_y:
            quadrants[0] += 1
        elif pos_y > midpoint_y:
            quadrants[1] += 1
    elif pos_x > midpoint_x:
        if pos_y < midpoint_y:
            quadrants[2] += 1
        elif pos_y > midpoint_y:
            quadrants[3] += 1
    
safety_factor = reduce(operator.mul, quadrants, 1)
print(safety_factor)