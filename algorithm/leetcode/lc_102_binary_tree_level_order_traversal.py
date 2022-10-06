import collections
from typing import List


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        out, level = [], [root]

        while level:
            out.append([node.val for node in level])
            next_level_nodes = [(node.left, node.right) for node in level]
            next_level_nodes_flat = [
                node for pair in next_level_nodes for node in pair if node]
            level = next_level_nodes_flat

        return out

    def levelOrderBFS(self, root):
        if not root:
            return []
        result = []

        queue = collections.deque([root])
        level = 0

        while queue:
            curr_level_len = len(queue)
            result.append([])
            for _ in range(curr_level_len):
                node = queue.pop(0)
                result[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return result

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = [root]
        res = []

        while que:
            level = []

            for _ in range(len(que)):
                node = que.pop(0)
                if node:
                    level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)

            if level:
                res.append(level)

        return res
