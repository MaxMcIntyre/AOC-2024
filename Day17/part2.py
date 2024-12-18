from part1 import run_program

with open('input.txt') as file:
    data = file.read()

_, program_text = data.split("\n\n")
program = list(map(int, program_text.split(": ")[1].split(",")))

def backtrack(program, curr_index, curr_register_val):
    if curr_index < 0:
        return curr_register_val
    else:
        curr_register_val *= 8
    
    for i in range(8):
        registers = {"A": curr_register_val + i, "B": 0, "C": 0}
        output = run_program(program, registers)
        if output[0] == program[curr_index]:
            possible = backtrack(program, curr_index - 1, curr_register_val + i)
            if possible > 0:
                return possible
    
    return 0

print(backtrack(program, len(program) - 1, 0))