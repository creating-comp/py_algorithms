#Best time to buy and sell stock
from itertools import chain

def func(array):
    map = {}
    for i in range(len(array)):
        ptr = i + 1
        while ptr < len(array):
            if array[i] not in map:
                map[array[i]] = []
            map[array[i]].append(array[i]-array[ptr])
            ptr += 1
    merged = list(chain.from_iterable(map.values()))
    return merged  # [1, 2, 3, 4, 5]

print(func([7, 1, 5, 3, 6,4]))
