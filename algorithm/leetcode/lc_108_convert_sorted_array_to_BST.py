# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        We use the range of [left, right], left inclusive, right inclusive.
    """
    def buildBST(self, nums, left, right) -> Optional[TreeNode]:
        if left > right:
            return None

        mid = (left + right) >> 1
        root = TreeNode(nums[mid])
        root.left = self.buildBST(nums, left, mid - 1)
        root.right = self.buildBST(nums, mid + 1, right)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sortedArray(nums, 0, len(nums) - 1)

    """
        Another way using slicing
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        root_index = (len(nums) - 1) >> 1

        root = TreeNode(nums[root_index])

        root.left = self.sortedArrayToBST(nums[:root_index])
        root.right = self.sortedArrayToBST(nums[root_index + 1:])

        return root