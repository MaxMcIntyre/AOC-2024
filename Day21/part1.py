from collections import deque

with open('input.txt') as file:
    codes = file.read().split("\n")

numeric_keypad = {"7": (0,0), "8": (0,1), "9": (0,2), "4": (1,0), "5": (1,1), "6": (1,2), "1": (2,0), "2": (2,1), "3": (2,2), "0": (3,1), "A": (3,2)}
directional_keypad = {"^": (0,1), "A": (0,2), "<": (1,0), "v": (1,1), ">": (1,2)}

numeric_grid = [["7","8","9"],["4","5","6"],["1","2","3"],[None,"0","A"]]
directional_grid = [[None,"^","A"],["<","v",">"]]

def calculate_paths(p1, p2, grid):
    y_diff, x_diff = p2[0] - p1[0], p2[1] - p1[1]
    y_dir = "v" if y_diff >= 0 else "^"
    x_dir = ">" if x_diff >= 0 else "<"
    y_move = 1 if y_diff >= 0 else -1
    x_move = 1 if x_diff >= 0 else -1

    queue = deque([(p1, "")])
    paths = []

    while queue:
        curr, directions = queue.popleft()
        if curr == p2:
            directions += "A"
            paths.append(directions)
        else:
            y, x = curr
            if y != p2[0] and grid[y + y_move][x]:
                directions_y = directions + y_dir
                queue.append(((y + y_move, x), directions_y))
            if x != p2[1] and grid[y][x + x_move]:
                directions_x = directions + x_dir
                queue.append(((y, x + x_move), directions_x))
    
    return paths

def find_directional_paths(paths):
    all_paths = []
    for path in paths:
        next_paths = [""]
        for i in range(len(path)):
            start = "A" if i == 0 else path[i-1]
            end = path[i]

            directional_paths = calculate_paths(directional_keypad[start], directional_keypad[end], directional_grid)
            next_paths = [path1 + path2 for path1 in next_paths for path2 in directional_paths]
        
        all_paths.extend(next_paths)
    
    return all_paths

if __name__ == "__main__":
    res = 0
    for code in codes:
        path_length = 0
        
        for i in range(len(code)):
            start = "A" if i == 0 else code[i-1]
            end = code[i]

            numeric_paths = calculate_paths(numeric_keypad[start], numeric_keypad[end], numeric_grid)
            directional_paths = find_directional_paths(numeric_paths)
            directional_paths_2 = find_directional_paths(directional_paths)

            path_length += min(len(path) for path in directional_paths_2)
    
        res += path_length * int(code[:-1])
    
    print(res)