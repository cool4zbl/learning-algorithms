from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        return self.sub(nums, [], ans)

    def sub(self, nums: List[int], res: List[int], ans: List[int]) -> List[List[int]]:
        if not nums:
            if res not in ans:
                ans.append(res)
            return ans

        self.sub(nums[1:], res + [], ans)
        self.sub(nums[1:], res + [nums[0]], ans)

        return ans


# nums = [1, 2, 2]
nums = [4, 4, 4, 1, 4]
print(Solution().subsetsWithDup(nums))
