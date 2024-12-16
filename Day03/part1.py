import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
res = 0

with open('input.txt') as file:
    matches = re.findall(pattern, file.read())
    for match in matches:
        res += int(match[0]) * int(match[1])

print(res)