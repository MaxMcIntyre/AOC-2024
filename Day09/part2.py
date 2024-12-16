from collections import defaultdict
import heapq

with open('input.txt') as file:
    data = file.read().strip()

id = 0
unfragmented = []
free_spaces = defaultdict(list)

for i in range(len(data)):
    if i % 2 == 0:
        unfragmented.extend([id] * int(data[i]))
        id += 1
    else:
        curr_pos = len(unfragmented)
        no_free_spaces = int(data[i])

        if no_free_spaces > 0:
            unfragmented.extend([-1] * no_free_spaces)
            heapq.heappush(free_spaces[no_free_spaces], curr_pos)

i = len(unfragmented) - 1
while i >= 0:
    if unfragmented[i] != -1:
        end = i
        id = unfragmented[end]

        while i >= 0 and unfragmented[i] == id:
            i -= 1
        start = i + 1
        min_length = (end - start) + 1

        actual_length = -1
        leftmost_block_start = len(unfragmented)
        for j in range(min_length, max(free_spaces) + 1):
            if free_spaces[j]:
                possible_block_start = free_spaces[j][0]
                if possible_block_start < start and possible_block_start < leftmost_block_start:
                    leftmost_block_start = possible_block_start
                    actual_length = j
        
        if actual_length >= 0:
            heapq.heappop(free_spaces[actual_length])

            for j in range(min_length):
                unfragmented[leftmost_block_start + j] = id
            if actual_length - min_length > 0:
                heapq.heappush(free_spaces[actual_length - min_length], leftmost_block_start + min_length)
            
            for j in range(min_length):
                unfragmented[start + j] = -1
    else:
        i -= 1

checksum = 0
for i in range(len(unfragmented)):
    if unfragmented[i] != -1:
        checksum += i * unfragmented[i]
print(checksum)