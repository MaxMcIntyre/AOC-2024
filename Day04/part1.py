with open('input.txt') as file:
    grid = file.read().splitlines()

directions = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
res = 0

for x in range(len(grid)):
    for y in range(len(grid[0])):
        for ni, nj in directions:
            i, j = x, y
            possible = []

            for k in range(4):
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                    possible.append(grid[i][j])
                    i, j = i + ni, j + nj
                else:
                    break
            
            possible = "".join(possible)
            if possible == "XMAS" or possible == "SAMX":
                res += 1

print(res // 2)