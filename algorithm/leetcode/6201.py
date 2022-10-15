from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        arr = [pref[0]]
        for i in range(1, n):
            arr.append(pref[i] ^ pref[i-1])
        return arr


pref = [5, 2, 0, 3, 1]
print(Solution().findArray(pref))
