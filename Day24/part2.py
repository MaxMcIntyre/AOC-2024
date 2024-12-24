# NOTE: This doesn't directly solve the problem, I just used the printed output
# to help manually work out the answer

with open('input.txt') as file:
    data = file.read()
    initial_values, equations = data.split("\n\n")
    initial_values = initial_values.split("\n")
    equations = equations.split("\n")

values = dict()

for initial_value in initial_values:
    var, value = initial_value.split(": ")
    values[var] = int(value)

full_equations = []

for equation in equations:
    expression, result = equation.split(" -> ")
    operand1, operator, operand2 = expression.split(" ")
    if operand1[0] == "y" and operand2[0] == "x":
        operand1, operand2 = operand2, operand1
    full_equations.append((operand1, operand2, operator, result))

full_equations.sort()
initial_sums = dict()
initial_carries = dict()
for i in range(len(full_equations)):
    operand1, operand2, operator, result = full_equations[i]
    if (operand1[0] == "x" and operand2[0] == "y"):
        if operator == "XOR":
            print(result, "is initial sum of", operand1, "and", operand2)
            initial_sums[result] = operand1[1:]
        elif operator == "AND":
            print(result, "is initial carry of", operand1, "and", operand2)
            initial_carries[result] = operand1[1:]

for i in range(len(full_equations)):
    operand1, operand2, operator, result = full_equations[i]
    if operator == "XOR":
        if operand1 in initial_sums:
            print(f"{result} is sum of {initial_sums[operand1]}")
        elif operand2 in initial_sums:
            print(f"{result} is sum of {initial_sums[operand2]}")
    if operator == "OR":
        if operand1 in initial_carries:
            print(f"{result} is carry of {initial_carries[operand1]}")
        elif operand2 in initial_carries:
            print(f"{result} is carry of {initial_carries[operand2]}")