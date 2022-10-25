from typing import List, Tuple, Optional
from collections import defaultdict, Counter
import math


class Solution:
    def countSubarrays(self, nums: List[int], min_k: int, max_k: int) -> int:
        ans = 0
        min_i = max_i = i0 = -1
        for i, x in enumerate(nums):
            if x == min_k:
                min_i = i
            if x == max_k:
                max_i = i
            if not min_k <= x <= max_k:
                i0 = i  # 子数组不能包含 nums[i0]
            ans += max(min(min_i, max_i) - i0, 0)
            # 注：上面这行代码，改为手动算 min max 会更快
            # j = min_i if min_i < max_i else max_i
            # if j > i0: ans += j - i0
        return ans

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        l, r1, r2, ret = -1, -1, -1, 0
        for i in range(len(nums)):
            if nums[i] > maxK or nums[i] < minK:
                l = i
            if nums[i] == maxK:
                r1 = i
            if nums[i] == minK:
                r2 = i
            ret += max(0, min(r1, r2) - l)
        return ret

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        l, r1, r2, ret = -1, -1, -1, 0
        for i in range(len(nums)):
            if nums[i] % 3 != 0:
                l = i
            c = 1
            for n in range(l, i):
                currentGCD = math.gcd(c, nums[n])
                c = currentGCD
                if currentGCD == 3:
                    r1 = n
                    ans += i - r1 + 1
        return ans

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for l in range(n):
            for r in range(l, n):
                ok = True
                res = []
                for i in range(l, r+1):
                    if nums[i] % 3 != 0:
                        ok = False
                        break
                    s = math.gcd(r[-1], nums[i])
                    r.append(s)
                    print('s=', s)
                    if s != 3:
                        ok = False
                        break
                    res.append(nums[i])
                if ok:
                    print(res)
                    count += 1
        return count


nums = [9, 3, 1, 2, 6, 3]
k = 3
print(Solution().subarrayGCD(nums, k))
