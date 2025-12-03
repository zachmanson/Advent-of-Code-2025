import os

dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir, "input.txt")

with open(file_path, 'r') as f:
    banks = [line.rstrip('\n') for line in f]

total = 0
for bank in banks:
    max_digit = max(bank[:-1])
    max_index = bank.index(max_digit)
    second_max_digit = max(bank[max_index + 1:])
    total += int(max_digit + second_max_digit)

print(total)

#part 2
def find_largest_joltage(bank: str) -> int:
    result = ''
    start = 0
    num_batteries = 12

    while num_batteries > 0:
        end = len(bank) - num_batteries + 1
        max_digit = max(bank[start:end])
        max_index = bank.index(max_digit, start, end)
        result += max_digit
        start = max_index + 1
        num_batteries -= 1

    return int(result)

total = 0
for bank in banks:
    total += find_largest_joltage(bank)

print(total)