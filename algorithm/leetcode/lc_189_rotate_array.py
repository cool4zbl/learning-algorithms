class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        idx = n - k

        # for _ in range(idx):
        # nums.append(nums.pop(0))
        # or

        for _ in range(k):
            nums.insert(0, nums.pop())
