from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        visited = [False] * len(nums)

        nums.sort()

        def backtracking(nums, res):
            # GOAL / base case
            if len(res) == n:
                ans.append(res[:])
                return

            for i in range(len(nums)):
                # CONSTRAINTs
                # if current element is duplicated of previous one
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue

                # Make CHOICE
                res.append(nums[i])

                # BACKTRACKING
                visited[i] = True
                backtracking(nums, res)

                # RESET STATE
                visited[i] = False
                res.pop()

        backtracking(nums, [])
        return ans
