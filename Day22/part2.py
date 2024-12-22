from part1 import calculate_next_secret

with open('input.txt') as file:
    secret_nums = list(map(int, file.read().split("\n")))

all_sequence_prices = dict()

for num in secret_nums:
    curr = num
    prices = [int(str(num)[-1])]

    for i in range(2000):
        curr = calculate_next_secret(curr)
        prices.append(int(str(curr)[-1]))
    
    price_differences = []
    for i in range(1, len(prices)):
        price_differences.append(prices[i] - prices[i-1])
    
    sequences_seen = set()
    for i in range(len(price_differences) - 3):
        sequence = tuple(price_differences[i:i+4])
        if sequence not in sequences_seen:
            all_sequence_prices[sequence] = all_sequence_prices.get(sequence, 0) + prices[i+4]
            sequences_seen.add(sequence)

max_bananas = max(all_sequence_prices.values())
print(max_bananas)