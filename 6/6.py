import os
import math

dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir, "input.txt")

with open(file_path, 'r') as f:
    raw_lines = [line.rstrip('\n') for line in f]

lines = [[int(c) if c.isdigit() else c for c in line.split(' ') if c != ''] for line in raw_lines]
columns = [col for col in zip(*lines)]

total = 0
for col in columns:
    operator = col[-1]
    if operator == '+':
        total += sum(col[:-1])
    else:
        total += math.prod(col[:-1])

print(total)

#part 2

#probably inefficient to compute all of this every time this function is called but i hate this problem and don't want to deal with it
def get_alignment(col_index: int) -> str:
    number_lines = raw_lines[:-1]  
    num_cols = len(number_lines[0])

    number_ranges = [] #indices of each block (columns) of numbers
    i = 0
    while i < num_cols:
        while i < num_cols and all(line[i] == ' ' for line in number_lines): #if entire col is spaces then that means those spaces are literally separating the numbers and not a part of alignemnt
            i += 1
        start = i
        while i < num_cols and not all(line[i] == ' ' for line in number_lines):
            i += 1
        end = i
        number_ranges.append((start, end))

    col_block = []
    for start, end in number_ranges:
        num = [line[start:end] for line in number_lines]
        col_block.append(num)

    for num_str in col_block[col_index]:
        if num_str[0] == ' ':
            return 'right'
        elif num_str[-1] == ' ':
            return 'left'

    return ''

total_p2 = 0
for prob_index, col in enumerate(columns):
    operator = col[-1]
    num_strs = [str(x) for x in col[:-1]]

    max_len = max(len(s) for s in num_strs)
    alignment = get_alignment(prob_index)

    #add in a filler 'x' to everything to make all the same size
    if alignment == 'left':
        num_strs = [x + 'x' * (max_len - len(x)) for x in num_strs]
    elif alignment == 'right':
        num_strs = ['x' * (max_len - len(x)) + x for x in num_strs]

    tranpose = [x for x in zip(*num_strs)]
    new_nums = [int(''.join(s).replace('x', '')) for s in tranpose] #removing the filler and converting to int

    if operator == '+':
        total_p2 += sum(new_nums)
    else:
        total_p2 += math.prod(new_nums)

print(total_p2)