with open('input.txt') as file:
    towels, designs = file.read().split("\n\n")
    towels = towels.split(", ")
    designs = designs.split("\n")

def backtrack(i, design):
    if i == len(design):
        return True
    
    for towel in towels:
        if i + len(towel) <= len(design) and design[i:i+len(towel)] == towel:
            if backtrack(i + len(towel), design):
                return True
    
    return False

possible_designs = 0
for design in designs:
    if backtrack(0, design):
        possible_designs += 1

print(possible_designs)