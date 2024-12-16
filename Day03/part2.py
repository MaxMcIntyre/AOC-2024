import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)"
res = 0

with open('input.txt') as file:
    data = file.read()
    matches = re.finditer(pattern, data)
    enabled = True
    
    for match in matches:
        if match.group(0) == "do()":
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
        else:
            if enabled:
                res += int(match.group(1)) * int(match.group(2))

print(res)