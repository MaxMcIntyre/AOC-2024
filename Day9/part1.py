with open('input.txt') as file:
    data = file.read().strip()

id = 0
unfragmented = []

for i in range(len(data)):
    if i % 2 == 0:
        unfragmented.extend([id] * int(data[i]))
        id += 1
    else:
        unfragmented.extend([-1] * int(data[i]))

left = 0
right = len(unfragmented) - 1
while left < right:
    if unfragmented[left] != -1:
        left += 1
    else:
        if unfragmented[right] == -1:
            right -= 1
        else:
            unfragmented[left] = unfragmented[right]
            unfragmented[right] = -1
            left += 1
            right -= 1

checksum = 0
i = 0
while unfragmented[i] != -1:
    checksum += i * unfragmented[i]
    i += 1

print(checksum)