from collections import Counter

left_list = []
right_list = []

with open('part1.txt') as file:
    for line in file:
        nums = line.split("   ")
        left_list.append(int(nums[0]))
        right_list.append(int(nums[1]))

res = 0
right_list_occurrences = Counter(right_list)

for num in left_list:
    res += num * right_list_occurrences.get(num, 0)

print(res)