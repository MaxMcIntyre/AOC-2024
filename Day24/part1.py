from collections import deque

with open('input.txt') as file:
    data = file.read()
    initial_values, equations = data.split("\n\n")
    initial_values = initial_values.split("\n")
    equations = equations.split("\n")

values = dict()

for initial_value in initial_values:
    var, value = initial_value.split(": ")
    values[var] = int(value)

operands = []
operators = []
outputs = []

for equation in equations:
    expression, result = equation.split(" -> ")
    operand1, operator, operand2 = expression.split(" ")
    operands.append((operand1, operand2))
    operators.append(operator)
    outputs.append(result)

queue = deque([i for i in range(len(operands))])

while queue:
    i = queue.popleft()
    (operand1, operand2), operator, output = operands[i], operators[i], outputs[i]
    if values.get(operand1) is not None and values.get(operand2) is not None:
        if operator == "OR":
            result = values[operand1] | values[operand2]
        elif operator == "AND":
            result = values[operand1] & values[operand2]
        else:
            result = values[operand1] ^ values[operand2]
        values[output] = result
    else:
        queue.append(i)
    
z_values = {i: values[i] for i in sorted(values) if i[0] == "z"}
res = 0
for multiplier, val in z_values.items():
    res += (2 ** int(multiplier[1:])) * val
print(res)