from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        DIRS = ((0, 1), (1, 0))

        ans = []
        m, n = len(grid), len(grid[0])

        def f(x, y, d):
            c = grid[x][y]
            x += DIRS[d][0]
            y += DIRS[d][1]

            if 0 <= x < m and 0 <= y < n:
                return f(x, y, d) + c
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if f(i, j, 0) % k == 0:
                    ans.append([i, j])

        def bfs(grid, k, res, m, n):
            if sum(res) % k == 0:
                ans.append(res[:])
                return

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    res.append(grid[i][j])
                    # print(res)
                    bfs(grid, k, res, m + 1, n)
                    bfs(grid, k, res, m, n + 1)
                    res.pop()
        bfs(grid, k, [], 0, 0)
        return ans


k = 3
grid = [[5, 2, 4], [3, 0, 5], [0, 7, 2]]
Solution().numberOfPaths(grid, 3)
