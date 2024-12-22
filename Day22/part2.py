from part1 import calculate_next_secret

with open('input.txt') as file:
    secret_nums = list(map(int, file.read().split("\n")))

all_sequence_prices = []
all_sequences = set()

for num in secret_nums:
    curr = num
    last_digits = [int(str(num)[-1])]

    for i in range(2000):
        curr = calculate_next_secret(curr)
        last_digits.append(int(str(curr)[-1]))
    
    price_differences = []
    for i in range(1, len(last_digits)):
        price_differences.append(last_digits[i] - last_digits[i-1])
    
    sequence_prices = dict()
    for i in range(len(price_differences) - 3):
        sequence = tuple(price_differences[i:i+4])
        if sequence not in sequence_prices:
            sequence_prices[sequence] = last_digits[i+4]
            all_sequences.add(sequence)
    
    all_sequence_prices.append(sequence_prices.copy())

max_bananas = 0
for sequence in all_sequences:
    bananas = 0
    for i in range(len(all_sequence_prices)):
        if sequence in all_sequence_prices[i]:
            bananas += all_sequence_prices[i][sequence]
    max_bananas = max(max_bananas, bananas)

print(max_bananas)