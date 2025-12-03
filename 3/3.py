import os

dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir, "input.txt")

with open(file_path, 'r') as f:
    banks = [line.rstrip('\n') for line in f]


def find_largest_joltage(bank: str, num_batteries: int) -> int:
    result = ''
    start = 0

    while num_batteries > 0:
        end = len(bank) - num_batteries + 1
        max_digit = max(bank[start:end])
        max_index = bank.index(max_digit, start, end)
        result += max_digit
        start = max_index + 1
        num_batteries -= 1

    return int(result)

total = 0
total_p2 = 0
for bank in banks:
    total += find_largest_joltage(bank, 2)
    total_p2 += find_largest_joltage(bank, 12)
    
print(total)
print(total_p2)