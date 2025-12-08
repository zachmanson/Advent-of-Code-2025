import os
import numpy as np
from itertools import combinations

dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir, "input.txt")

with open(file_path, 'r') as f:
    lines = [line.rstrip('\n') for line in f]

boxes = [(int(x), int(y), int(z)) for x, y, z in (line.split(',') for line in lines)]
combs = list(combinations(boxes, 2))

def distance(pos1: tuple[int, int, int], pos2: tuple[int, int, int]) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

# this was too slow
# def find_closest_pair(seen: set[tuple[tuple[int, int, int], tuple[int, int, int]]]) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
#     unseen_combs = [pair for pair in combs if pair not in seen]
#     return min(unseen_combs, key = lambda pair: distance(pair[0], pair[1]))

pair_distances = [(pair, distance(*pair)) for pair in combs]
pair_distances.sort(key = lambda x: x[1])

circuits = []
seen = set()

#this does ignore the circuits which are just a single box but we only need biggest three circuits anyway
i = 0 
while i < 1000:
    pair = pair_distances[i][0]
    if pair in seen or (pair[1], pair[0]) in seen:
        i += 1
        continue
    seen.add(pair)
    box1, box2 = pair
    circuits_to_connect = [c for c in circuits if box1 in c or box2 in c]

    if not circuits_to_connect:
        circuits.append({box1, box2})
    else:
        merged = set()
        for c in circuits_to_connect:
            merged = merged | c
        merged = merged | {box1, box2}

        for c in circuits_to_connect:
            circuits.remove(c)

        circuits.append(merged)

    i += 1

circuits.sort(key = lambda x: len(x), reverse = True)
ans = len(circuits[0]) * len(circuits[1]) * len(circuits[2])
print(ans)

#part 2. Going to be a lot of repeat code but it's late and i dont want to merge it all

circuits = []
seen = set()

i = 0
while True:
    pair = pair_distances[i][0]
    if pair in seen or (pair[1], pair[0]) in seen:
        i += 1
        continue
    seen.add(pair)
    box1, box2 = pair
    circuits_to_connect = [c for c in circuits if box1 in c or box2 in c]

    if not circuits_to_connect:
        circuits.append({box1, box2})
    else:
        merged = set()
        for c in circuits_to_connect:
            merged = merged | c
        merged = merged | {box1, box2}

        for c in circuits_to_connect:
            circuits.remove(c)

        circuits.append(merged)

    if all(box in circuits[0] for box in boxes):
        print(box1[0] * box2[0])
        break

    i += 1