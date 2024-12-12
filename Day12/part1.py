with open('input.txt') as file:
    data = file.readlines()

grid = [list(line.strip()) for line in data]

total_cost = 0
directions = [(-1,0),(1,0),(0,-1),(0,1)]
visited = set()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) not in visited:
            region_area = 0
            region_perimeter = 0
            curr_region = grid[i][j]
            stack = [(i, j)]
            visited.add((i, j))

            while stack:
                x, y = stack.pop()
                region_area += 1

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                        if grid[nx][ny] != curr_region:
                            region_perimeter += 1
                        elif (nx, ny) not in visited:
                            stack.append((nx, ny))
                            visited.add((nx, ny))
                    else:
                        region_perimeter += 1
            
            print(curr_region, region_area, region_perimeter)
            total_cost += region_area * region_perimeter
    
print(total_cost)