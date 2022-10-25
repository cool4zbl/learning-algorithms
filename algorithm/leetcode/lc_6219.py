from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            neg = ~nums[i] + 1
            if neg in nums:
                return nums[i]
        return -1
