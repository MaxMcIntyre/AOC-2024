from collections import deque

def find_path(grid):
    directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
    visited = set([(0, 0)])
    queue = deque([((0, 0), None)])
    prevs = dict()

    while queue:
        (x, y), prev = queue.popleft()
        prevs[(x, y)] = prev
        if x == 70 and y == 70:
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#" and (nx, ny) not in visited:
                queue.append(((nx, ny), (x, y)))
                visited.add((nx, ny))
    
    curr = (70, 70)
    path = set()
    if not prevs.get(curr):
        return path
    
    while curr:
        path.add(curr)
        curr = prevs[curr]
    return path

if __name__ == "__main__":
    with open('input.txt') as file:
        positions = list(map(lambda x: tuple(map(int, x.split(','))), file.read().split("\n")))

    grid = [["." for _ in range(71)] for _ in range(71)]

    for i in range(1024):
        pos_x, pos_y = positions[i]
        grid[pos_x][pos_y] = "#"
    
    path = find_path(grid)
    print(len(path) - 1)