with open('input.txt') as file:
    data = file.readlines()

grid = [list(line.strip()) for line in data]

total_cost = 0
directions = [(0,-1),(-1,0),(0,1),(1,0)]
visited = set()

def find_corners(x, y, region):
    corners = 0

    for i in range(len(directions)):
        dx1, dy1 = directions[i]
        dx2, dy2 = directions[(i + 1) % len(directions)]

        side1_x, side1_y = x + dx1, y + dy1
        side1 = grid[side1_x][side1_y] if 0 <= side1_x < len(grid) and 0 <= side1_y < len(grid[0]) else ""

        side2_x, side2_y = x + dx2, y + dy2
        side2 = grid[side2_x][side2_y] if 0 <= side2_x < len(grid) and 0 <= side2_y < len(grid[0]) else ""

        corner_x, corner_y = x + dx1 + dx2, y + dy1 + dy2
        corner = grid[corner_x][corner_y] if 0 <= corner_x < len(grid) and 0 <= corner_y < len(grid[0]) else ""

        if (side1 != region and side2 != region) or (side1 == region and side2 == region and corner != region):
            corners += 1
    
    return corners

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) not in visited:
            region_area = 0
            region_sides = 0
            curr_region = grid[i][j]
            stack = [(i, j)]
            visited.add((i, j))

            while stack:
                x, y = stack.pop()
                region_area += 1

                region_sides += find_corners(x, y, curr_region)

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                        if (nx, ny) not in visited and grid[nx][ny] == curr_region:
                            stack.append((nx, ny))
                            visited.add((nx, ny))
            
            total_cost += region_area * region_sides

print(total_cost)