from typing import List


class Solution:
    """
        TC: O(n * 2^n)
        SC: O(n * 2^n)
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        return self.sub(nums, [], ans)

    def sub(self, nums: List[int], res: List[int], ans: List[int]) -> List[List[int]]:
        if not nums:
            ans.append(res)
            return ans

        # for each num, there're only two kinds in the current combination - exist or non-exist
        self.sub(nums[1:], res + [], ans)
        self.sub(nums[1:], res + [nums[0]], ans)

        return ans

    """
        backtracking
        TC: O(n * 2^n)
        SC: O(n)
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                ans.append(curr[:])
                return

            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next elements to complete the combination
                backtrack(i+1, curr)
                # backtrack
                curr.pop()

        ans = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()

        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(nums, res, k):
            ans.append(res[:])

            for i in range(k, len(nums)):
                res.append(nums[i])
                backtracking(nums, res, i+1)
                res.pop()

        backtracking(nums, [], 0)
        return ans


nums = [1, 2, 3]
print(Solution().subsets(nums))
