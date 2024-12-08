left_list = []
right_list = []

with open('input.txt') as file:
    for line in file:
        nums = line.split("   ")
        left_list.append(int(nums[0]))
        right_list.append(int(nums[1]))

left_list.sort()
right_list.sort()

res = 0
for i in range(len(left_list)):
    res += abs(left_list[i] - right_list[i])

print(res)