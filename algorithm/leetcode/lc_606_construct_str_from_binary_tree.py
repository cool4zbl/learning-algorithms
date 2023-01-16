from typing import List, Tuple, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        stack = []
        stack.push(root)
        visited = set()
        res = []

        while len(stack):
            node = stack[-1]
            if node in visited:
                stack.pop()
                res.append(")")
            else:
                visited.add(node)
                res.append("(" + node.val)
                if not node.left and not node.right:
                    res.append("()")
                if node.right:
                    stack.push(node.right)
                if node.left:
                    stack.push(node.left)

        return ''.join(res[1:-1])

    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(t, ans):
            if not t:
                return
            ans.append(str(t.val))
            if not t.left and not t.right:
                return ans
            ans.append("(")
            dfs(t.left, ans)
            ans.append(")")
            if t.right:
                ans.append("(")
                dfs(t.right, ans)
                ans.append(")")

        res = []

        dfs(root, res)
        print(res)
        return ''.join(res)
