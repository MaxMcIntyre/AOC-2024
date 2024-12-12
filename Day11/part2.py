from collections import defaultdict

with open('input.txt') as file:
    data = file.read()

stone_counts = defaultdict(int)
for char in data.split():
    stone_counts[int(char)] += 1

for i in range(75):
    next_stone_counts = defaultdict(int)
    for stone, count in stone_counts.items():
        if stone == 0:
            next_stone_counts[1] += count
        else:
            stone_str = str(stone)
            if len(stone_str) % 2 == 0:
                next_stone_counts[int(stone_str[len(stone_str) // 2:])] += count
                next_stone_counts[int(stone_str[:len(stone_str) // 2])] += count
            else:
                next_stone_counts[stone * 2024] += count
    
    stone_counts = next_stone_counts

print(sum(stone_counts.values()))