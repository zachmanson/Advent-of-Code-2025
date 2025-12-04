import os
from collections import deque

dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir, "input.txt")

with open(file_path, 'r') as f:
    grid = [line.rstrip('\n') for line in f]

MAX_ROW = len(grid)
MAX_COL = len(grid[0])

DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))

def is_in_bounds(r: int, c: int) -> bool:
    return 0 <= r < MAX_ROW and 0 <= c < MAX_COL

def count_adj_rolls(row: int, col: int) -> int:
    adj_rolls = 0
    for dr, dc in DIRS:
        new_row = row + dr 
        new_col = col + dc
        if is_in_bounds(new_row, new_col) and grid[new_row][new_col] == '@':
            adj_rolls += 1

    return adj_rolls

to_remove = set() #for part 2
total = 0
for row in range(MAX_ROW):
    for col in range(MAX_COL):
        if grid[row][col] == '@':
            num_adj_rolls = count_adj_rolls(row, col)
            if num_adj_rolls < 4:
                to_remove.add((row, col))
                total += 1

print(total)

#part 2

def get_all_neighbors(row: int, col: int) -> list[tuple[int, int]]:
    neighbors = []
    for dr, dc in DIRS:
        new_row = row + dr
        new_col = col + dc
        if is_in_bounds(new_row, new_col) and grid[new_row][new_col] == '@': 
            neighbors.append((new_row, new_col))

    return neighbors

def can_remove(row: int, col: int) -> bool:
    return count_adj_rolls(row, col) < 4 and grid[row][col] == '@'

grid = [list(row) for row in grid] # convert grid to list of lists to be mutable

to_check = deque() #only need to check the neighboring '@' of the ones we remove
#was originally keeping a 'seen' set but that causes me to undercount becuase if roll can't be removed now doesn't mean it can't be removed later as the grid updates

#remove all rolls from p1
for row, col in to_remove:
    grid[row][col] = '.'
    for n in get_all_neighbors(row, col):
        to_check.append(n)

total_p2 = len(to_remove)

while to_check:
    row, col = to_check.popleft() #thought order of removal matters but .pop() also gives the same ans
    if can_remove(row, col):
        grid[row][col] = '.'
        total_p2 += 1
        neighbors = get_all_neighbors(row, col)
        for n in neighbors:
            to_check.append(n)

print(total_p2)