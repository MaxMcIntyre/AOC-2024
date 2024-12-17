import re

def find_combo(operand, registers):
    match operand:
        case n if 0 <= n <= 3:
            return n
        case 4:
            return registers["A"]
        case 5:
            return registers["B"]
        case 6:
            return registers["C"]

def divide(reg, operand, registers):
    res = registers["A"] // (2 ** operand)
    registers[reg] = res

def bitwise_xor(operand1, operand2, registers):
    res = operand1 ^ operand2
    registers["B"] = res

def modulo(operand, registers):
    res = operand % 8
    registers["B"] = res

def jump(pc, operand, registers):
    return pc if registers["A"] == 0 else operand

def run_program(program, registers):
    output = []
    i = 0

    while i < len(program):
        opcode = program[i]
        does_jump = False

        match opcode:
            case 0:
                combo = find_combo(program[i+1], registers)
                divide("A", combo, registers)
            case 1:
                bitwise_xor(registers["B"], program[i+1], registers)
            case 2:
                combo = find_combo(program[i+1], registers)
                modulo(combo, registers)
            case 3:
                new_pc = jump(i, program[i+1], registers)
                if new_pc != i:
                    does_jump = True
                    i = new_pc
            case 4:
                bitwise_xor(registers["B"], registers["C"], registers)
            case 5:
                combo = find_combo(program[i+1], registers)
                output.append(combo % 8)
            case 6:
                combo = find_combo(program[i+1], registers)
                divide("B", combo, registers)
            case 7:
                combo = find_combo(program[i+1], registers)
                divide("C", combo, registers)
        
        if not does_jump:
            i += 2
    
    return output

if __name__ == "__main__":
    with open('input.txt') as file:
        data = file.read()

    register_text, program_text = data.split("\n\n")
    registers = dict()
    registers["A"] = int(re.search(r"Register A: (\d+)", register_text).group(1))
    registers["B"] = int(re.search(r"Register B: (\d+)", register_text).group(1))
    registers["C"] = int(re.search(r"Register C: (\d+)", register_text).group(1))
    program = list(map(int, program_text.split(": ")[1].split(",")))

    output = run_program(program, registers)
    print(",".join(map(str, output)))