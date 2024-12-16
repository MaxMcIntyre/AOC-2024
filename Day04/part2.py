with open('input.txt') as file:
    grid = file.read().splitlines()

res = 0

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == "A" and 0 < x < len(grid) - 1 and 0 < y < len(grid[0]) - 1:
            left_diagonal = "".join([grid[x-1][y-1], grid[x][y], grid[x+1][y+1]])
            right_diagonal = "".join([grid[x-1][y+1], grid[x][y], grid[x+1][y-1]])
            if (left_diagonal == "MAS" or left_diagonal == "SAM") and (right_diagonal == "MAS" or right_diagonal == "SAM"):
                res += 1

print(res)