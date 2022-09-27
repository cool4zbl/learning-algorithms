from typing import List


class Solution:
    def longest(self, nums: List[int]) -> int:
        max_num = max(nums)
        ans = 0
        cur = 0

        for n in nums:
            if n == max_num:
                cur += 1
            else:
                cur = 0

            ans = max(ans, cur)
        return ans


n4 = [3, 3, 2, 1, 3, 3, 3]  # 3
n3 = [96317, 96317, 96317, 96317, 96317,
      96317, 96317, 96317, 96317, 279979]  # 1
n2 = [1, 2, 3, 3, 2, 2, 3]  # 2

n1 = [311155, 311155, 311155, 311155, 311155,
      311155, 311155, 311155, 201191, 311155]  # 8

print(Solution().longest(n4))
print(Solution().longest(n3))
print(Solution().longest(n2))
print(Solution().longest(n1))
