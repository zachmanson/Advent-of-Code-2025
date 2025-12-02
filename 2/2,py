import os

dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir, "input.txt")

with open(file_path, 'r') as f:
    data = [line.rstrip('\n') for line in f][0]

ids = data.split(',')

total = 0
for id in ids:
    beginning, end = map(int, id.split('-'))

    for i in range(beginning, end + 1):
        num_str = str(i)
        if len(num_str) % 2 == 0:
            if num_str[:len(num_str) // 2] == num_str[len(num_str) // 2:]:
                total += i

print(total)

#part 2
def count_invalid_ids(ids: list[str]) -> int:
    total = 0
    seen = set()

    for id in ids:
        beginning, end = map(int, id.split('-'))
        min_digits = len(str(beginning))
        max_digits = len(str(end))

        for digits in range(min_digits, max_digits + 1):
            for sequence_length in range(1, digits):
                if digits % sequence_length != 0:
                    continue
                
                num_repeats = digits // sequence_length

                sequence_beginning = 10**(sequence_length - 1)
                sequence_end = 10**(sequence_length) - 1

                for sequence in range(sequence_beginning, sequence_end + 1):
                    repeated_seq = int(str(sequence) * num_repeats)
                    if beginning <= repeated_seq <= end:
                        if repeated_seq not in seen:
                            total += repeated_seq
                            seen.add(repeated_seq)

    return total

print(count_invalid_ids(ids))