import re

with open('input.txt') as file:
    entries = file.read().split("\n\n")

total_tokens = 0

for entry in entries:
    button_a_vals = re.search(r"A: X\+(\d+), Y\+(\d+)", entry)
    button_b_vals = re.search(r"B: X\+(\d+), Y\+(\d+)", entry)
    prize_vals = re.search(r"Prize: X=(\d+), Y=(\d+)", entry)

    button_a = (int(button_a_vals.group(1)), int(button_a_vals.group(2)))
    button_b = (int(button_b_vals.group(1)), int(button_b_vals.group(2)))
    prize = (int(prize_vals.group(1)), int(prize_vals.group(2)))

    tokens_needed = float('inf')

    for i in range(1, 101):
        for j in range(1, 101):
            location = (button_a[0] * i + button_b[0] * j, button_a[1] * i + button_b[1] * j)
            if location == prize:
                tokens_needed = min(tokens_needed, 3 * i + j)
    
    if tokens_needed != float('inf'):
        total_tokens += tokens_needed

print(total_tokens)