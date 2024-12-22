with open('input.txt') as file:
    secret_nums = list(map(int, file.read().split("\n")))

def mix_prune(num, next_num):
    num = num ^ next_num
    return num % 16777216

def calculate_next_secret(num):
    next_num = num * 64
    num = mix_prune(num, next_num)
    next_num = num // 32
    num = mix_prune(num, next_num)
    next_num = num * 2048
    num = mix_prune(num, next_num)
    return num


if __name__ == "__main__":
    res = 0
    for num in secret_nums:
        curr = num
        for i in range(2000):
            curr = calculate_next_secret(curr)
        res += curr
    print(res)