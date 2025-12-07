import os
from collections import deque
from functools import lru_cache

dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir, "input.txt")

with open(file_path, 'r') as f:
    grid = [line.rstrip('\n') for line in f]

NUM_ROWS = len(grid)
NUM_COLS = len(grid[0])

def is_in_bounds(row, col):
    return 0 <= row < NUM_ROWS and 0 <= col < NUM_COLS

start = (0, grid[0].index('S'))
beams = deque([start])

num_splits = 0
seen = set()

while beams:
    row, col = beams.popleft()
    
    if not is_in_bounds(row, col):
        continue

    if grid[row][col] in ['S', '.']:
        if (row + 1, col) not in seen:
            seen.add((row + 1, col))
            beams.append((row + 1, col))
    elif grid[row][col] == '^':
        num_splits += 1
        if (row, col + 1) not in seen:
            seen.add((row, col + 1))
            beams.append((row, col + 1))
        if (row, col - 1) not in seen:
            seen.add((row, col - 1))
            beams.append((row, col - 1))

print(num_splits)

#part 2
@lru_cache(None)
def count_timelines(row, col):
    if not is_in_bounds(row, col):
        return 1
    if grid[row][col] in ['S', '.']:
        return count_timelines(row + 1, col) #just go down
    elif grid[row][col] == '^':
        return count_timelines(row, col - 1) + count_timelines(row, col + 1) #left and right paths
    
    return 0
    
print(count_timelines(*start))

