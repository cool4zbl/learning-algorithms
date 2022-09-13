class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
            Use binary search to find the index.
            Search range [lo, hi)
            If we find the index of target, return the index directly.
            Otherwise, return the low/high index.
        """

        lo, hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) >> 1

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1

        return hi
