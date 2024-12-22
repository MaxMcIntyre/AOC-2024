from part1 import calculate_paths

with open('input.txt') as file:
    codes = file.read().split("\n")

numeric_keypad = {"7": (0,0), "8": (0,1), "9": (0,2), "4": (1,0), "5": (1,1), "6": (1,2), "1": (2,0), "2": (2,1), "3": (2,2), "0": (3,1), "A": (3,2)}
directional_keypad = {"^": (0,1), "A": (0,2), "<": (1,0), "v": (1,1), ">": (1,2)}

numeric_grid = [["7","8","9"],["4","5","6"],["1","2","3"],[None,"0","A"]]
directional_grid = [[None,"^","A"],["<","v",">"]]

def find_recursive_paths(path, depth, memo):
    if depth == 25:
        return len(path)
    elif (path, depth) in memo:
        return memo[(path, depth)]

    min_length_path = 0
    for i in range(len(path)):
        start = "A" if i == 0 else path[i-1]
        end = path[i]

        min_length_path += min(find_recursive_paths(next_subpath, depth + 1, memo) for next_subpath in calculate_paths(directional_keypad[start], directional_keypad[end], directional_grid))

    memo[(path, depth)] = min_length_path
    
    return min_length_path

res = 0
for code in codes:
    path_length = 0
    memo = dict()

    for i in range(len(code)):
        start = "A" if i == 0 else code[i-1]
        end = code[i]
        
        numeric_paths = calculate_paths(numeric_keypad[start], numeric_keypad[end], numeric_grid)
        path_length += min(find_recursive_paths(path, 0, memo) for path in numeric_paths)
    
    res += path_length * int(code[:-1])
    
print(res)