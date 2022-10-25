from typing import List, Tuple, Optional
from collections import defaultdict, Counter
# from sortedcontainers import SortedList


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        e1, e2 = [], []
        for e in event1:
            h, m0 = e.split(":")
            m = int(m0) / 60

            e1.append(int(h) + m)
        for e in event2:
            h, m0 = e.split(":")
            m = int(m0) / 60

            e2.append(int(h) + m)

        return not (e1[1] < e2[0] or e2[1] < e1[0])


event1 = ["01:15", "02:00"]
event2 = ["02:00", "03:00"]
print(Solution().haveConflict(event1, event2))
event1 = ["01:00", "02:00"]
event2 = ["01:20", "03:00"]
print(Solution().haveConflict(event1, event2))
event1 = ["10:00", "11:00"]
event2 = ["14:00", "15:00"]
print(Solution().haveConflict(event1, event2))
