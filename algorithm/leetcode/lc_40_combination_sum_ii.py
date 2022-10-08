from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # cannot contain duplicates.
        candidates.sort()

        def backtracking(candidates, target, res, k):
            if sum(res) == target:
                ans.append(res[:])
                return

            for i in range(k, len(candidates)):
                if sum(res) + candidates[i] > target:
                    break

                # `1a, 1b...`, here skip `1b`
                if i > k and candidates[i-1] == candidates[i]:
                    continue

                res.append(candidates[i])
                backtracking(candidates, target, res, i + 1)
                res.pop()

        backtracking(candidates, target, [], 0)

        return ans
