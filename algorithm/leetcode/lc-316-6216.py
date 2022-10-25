from typing import List, Tuple, Optional
from collections import defaultdict, Counter
import sys


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        m = sys.maxsize
        for i in range(n):
            s = 0
            for j in range(n):
                s += abs((nums[j] - nums[i])) * cost[j]

            if s < m:
                m = s
        print(m)


nums = [1, 3, 5, 2]
cost = [2, 3, 1, 14]
Solution().minCost(nums, cost)
nums = [2, 2, 2, 2, 2]
cost = [4, 2, 8, 1, 3]
Solution().minCost(nums, cost)
