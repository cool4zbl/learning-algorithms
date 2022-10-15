from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def isInArea(grid, r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        m = len(grid)
        n = len(grid[0])

        def dfs(grid, r, c):
            # if not isInArea(grid, r, c):
            #     return

            print(r, c)
            if not (0 <= r < m and 0 <= c < n):
                return

            if grid[r][c] != '1':
                return

            grid[r][c] = '2'
            dfs(grid, r-1, c)
            dfs(grid, r, c+1)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    count += 1
                    dfs(grid, r, c)
        print(grid)
        return count

    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     nr = len(grid)
    #     if nr == 0:
    #         return 0
    #     nc = len(grid[0])

    #     num_islands = 0
    #     for r in range(nr):
    #         for c in range(nc):
    #             if grid[r][c] == "1":
    #                 num_islands += 1
    #                 self.dfs(grid, r, c)

    #     return num_islands


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(Solution().numIslands(grid))
