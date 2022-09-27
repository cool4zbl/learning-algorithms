from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        return self.sub(nums, [], ans)

    def sub(self, nums: List[int], res: List[int], ans: List[int]) -> List[List[int]]:
        if not nums:
            ans.append(res)
            return ans

        self.sub(nums[1:], res + [nums[0]], ans)
        self.sub(nums[1:], res + [], ans)

        return ans


nums = [1, 2, 3]
print(Solution().subsets(nums))
