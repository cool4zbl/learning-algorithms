from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        def backtracking(nums, res, k):
            ans.append(res[:])

            for i in range(k, len(nums)):
                if i > k and nums[i] == nums[i-1]:
                    continue

                res.append(nums[i])
                backtracking(nums, res, i + 1)
                res.pop()

        backtracking(nums, [], 0)
        return ans


# nums = [1, 2, 2]
nums = [4, 4, 4, 1, 4]
print(Solution().subsetsWithDup(nums))
