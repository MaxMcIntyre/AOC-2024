res = 0

with open('input.txt') as file:
    for line in file:
        report = [int(num) for num in line.split()]
        increasing = report[0] <= report[1]
        is_safe = True

        for i in range(1, len(report)):
            if (increasing and report[i-1] >= report[i]) or (not increasing and report[i-1] <= report[i]) or (not 1 <= abs(report[i] - report[i-1]) <= 3):
                is_safe = False
        
        if is_safe:
            res += 1

print(res)