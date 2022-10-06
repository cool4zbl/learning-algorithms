from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtracking(candidates, target, res, k):
            if sum(res) == target:
                ans.append(res[:])
                return
            for i in range(k, len(candidates)):
                if sum(res) + candidates[i] > target:
                    continue

                res.append(candidates[i])
                backtracking(candidates, target, res, i)
                res.pop()

        backtracking(candidates, target, [], 0)
        return ans


can = [2, 3, 6, 7]
target = 7
can = [2, 3, 5]
target = 8
print(Solution().combinationSum(can, target))
