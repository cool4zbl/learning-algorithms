class Solution:

    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) >> 1
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return lo

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = self.search(nums, target)

        """
            `target in nums[lo:lo+1]` instead of target == nums[lo] to prevent from "list index out of range"

            We need to find the lower_bound and upper_bound.
            Find the nums's lower_bound, which index is "the first value of target".
            Find the num’s upper_bound, which index is "first value is target + 1",
            i.e. find the lower_bound of "target + 1", so we can reuse the same method by binary search.
        """
        return [lo, self.search(nums, target + 1) - 1] if target in nums[lo:lo+1] else [-1, -1]