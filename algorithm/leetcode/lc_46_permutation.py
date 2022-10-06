from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = [False] * len(nums)
        n = len(nums)

        def backtracking(nums, res, visited):
            if len(res) == n:
                ans.append(res[:])
                return

            for i in range(len(nums)):
                if not visited[i]:
                    res.append(nums[i])
                    visited[i] = True

                    backtracking(nums, res, visited)
                    visited[i] = False
                    res.pop()

        backtracking(nums, [], visited)
        return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtracking(nums, res):
            if len(res) == n:
                # or
                # if len(nums) == 0:
                ans.append(res[:])
                return

            for i in range(len(nums)):
                res.append(nums[i])
                backtracking(nums[0:i] + nums[i+1:], res)
                res.pop()

        backtracking(nums, [])
        return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(nums, level):
            if level == len(nums) - 1:
                ans.append(nums[:])
                return
            for i in range(level, len(nums)):
                nums[i], nums[level] = nums[level], nums[i]
                backtracking(nums, level + 1)
                nums[i], nums[level] = nums[level], nums[i]
        backtracking(nums, 0)
        return ans
