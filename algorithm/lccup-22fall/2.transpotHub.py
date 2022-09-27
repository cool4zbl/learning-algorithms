from collections import defaultdict
from typing import List


def transportationHub(path: List[List[int]]) -> int:
    indeg = [0] * 1000
    outdeg = [0] * 1000

    station = set()

    for p in path:
        start, end = p
        indeg[end] += 1
        outdeg[start] += 1
        station.add(start)
        station.add(end)

    n = len(station)

    for s in station:
        if indeg[s] == n - 1 and outdeg[s] == 0:
            return s

    return -1


l = [[0, 1], [0, 3], [1, 3], [2, 0], [2, 3]]
print(transportationHub(l))
l1 = [[0, 3], [1, 0], [1, 3], [2, 0], [3, 0], [3, 2]]
print(transportationHub(l1))
