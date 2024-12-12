with open('input.txt') as file:
    data = file.read()

stones = [int(char) for char in data.split()]

for i in range(25):
    next_stones = []

    for stone in stones:
        if stone == 0:
            next_stones.append(1)
        else:
            stone_str = str(stone)
            if len(stone_str) % 2 == 0:
                next_stones.append(int(stone_str[len(stone_str) // 2:]))
                next_stones.append(int(stone_str[:len(stone_str) // 2]))
            else:
                next_stones.append(stone * 2024)
    
    stones = next_stones

print(len(next_stones))