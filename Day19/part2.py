with open('input.txt') as file:
    towels, designs = file.read().split("\n\n")
    towels = towels.split(", ")
    designs = designs.split("\n")

def backtrack(i, design, memo):
    if i == len(design):
        return 1
    
    if i in memo:
        return memo[i]
    
    ways = 0
    for towel in towels:
        if i + len(towel) <= len(design) and design[i:i+len(towel)] == towel:
            ways += backtrack(i + len(towel), design, memo)
    
    memo[i] = ways
    return ways

total_designs = 0
for design in designs:
    memo = dict()
    total_designs += backtrack(0, design, memo)

print(total_designs)