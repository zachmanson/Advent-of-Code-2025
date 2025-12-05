import os

dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir, "input.txt")

with open(file_path, 'r') as f:
    lines = [line.rstrip('\n') for line in f]

empty_space = lines.index('')
fresh_ingredients = lines[:empty_space]
avail_ingredients = lines[empty_space + 1:]

fresh_ranges = [tuple(map(int, r.split('-'))) for r in fresh_ingredients]

total = 0 
for i in avail_ingredients:
    if any([low <= int(i) <= high for low, high in fresh_ranges]):
        total += 1

print(total)

#part 2

fresh_ranges = sorted(fresh_ranges, key = lambda x: x[0])
merged = [(fresh_ranges[0][0], fresh_ranges[0][1])]
for start, end in fresh_ranges[1:]:
    last_start, last_end = merged[-1]
    if start <= last_end:
        merged[-1] = (last_start, max(last_end, end))
    else:
        merged.append((start, end))

total_p2 = 0
for start, end in merged:
    total_p2 += (end - start + 1)
print(total_p2)