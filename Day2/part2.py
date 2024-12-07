def check_level_safe(report, can_remove):
    increasing = report[0] <= report[1]
    for i in range(len(report) - 1):
        if (increasing and report[i] >= report[i+1]) or (not increasing and report[i] <= report[i+1]) or (not 1 <= abs(report[i] - report[i+1]) <= 3):
            if not can_remove:
                return False
            else:
                return check_level_safe(report[:i-1] + report[i:], False) or check_level_safe(report[:i] + report[i+1:], False) or check_level_safe(report[:i+1] + report[i+2:], False)
    
    return True

res = 0

with open('input.txt') as file:
    for line in file:
        report = [int(num) for num in line.split()]
        is_safe = check_level_safe(report, True)
        
        if is_safe:
            res += 1

print(res)