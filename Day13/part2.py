from sympy import symbols, Eq, solve
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
    prize = (int(prize_vals.group(1)) + 10000000000000, int(prize_vals.group(2)) + 10000000000000)

    tokens_needed = float('inf')

    a, b = symbols('a b')
    eq1 = Eq(button_a[0] * a + button_b[0] * b, prize[0])
    eq2 = Eq(button_a[1] * a + button_b[1] * b, prize[1])

    solution = solve((eq1, eq2), (a, b))

    if solution and solution[a].is_integer and solution[b].is_integer:
        total_tokens += 3 * solution[a] + solution[b]

print(total_tokens)