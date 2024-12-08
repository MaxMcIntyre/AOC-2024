all_answers = []
all_numbers = []

with open('input.txt') as file:
    for line in file:
        answer, numbers = line.split(":")
        all_answers.append(int(answer))
        all_numbers.append([int(number) for number in numbers.strip().split(" ")])

for i in range(len(all_answers)):
    print(all_answers[i], all_numbers[i])

def calculate_calibration_result(answer, numbers):
    def backtrack(i, curr):
        if i == len(numbers):
            return curr == answer
        elif curr > answer:
            return False
        else:
            curr_add = curr + numbers[i]
            curr_multiply = curr * numbers[i]
            curr_concat = int(str(curr) + str(numbers[i]))

            return backtrack(i + 1, curr_add) or backtrack(i + 1, curr_multiply) or backtrack(i + 1, curr_concat)
    
    return answer if backtrack(1, numbers[0]) else 0

total_calibration_result = 0
for i in range(len(all_answers)):
    total_calibration_result += calculate_calibration_result(all_answers[i], all_numbers[i])
print(total_calibration_result)