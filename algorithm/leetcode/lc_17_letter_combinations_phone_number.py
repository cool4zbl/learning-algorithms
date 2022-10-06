from typing import List


class Solution:
    """
        backtracking
    """

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        ans = []
        n = len(digits)

        def backtracking(digits, res, k):
            if len(res) == n:
                ans.append(''.join(res))
                return

            # pruning
            for i in range(k, len(digits)):
                for c in d_map[digits[i]]:
                    res.append(c)
                    backtracking(digits[0:i]+digits[i+1:], res, i)
                    res.pop()

        backtracking(digits, [], 0)
        return ans

    """
        non-recursive way
    """

    def letterCombinations(self, digits: str) -> List[str]:
        d_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        combs = [''] if digits else []
        for d in digits:
            combs = [p + q for p in combs for q in d_map[d]]
        return combs


Solution().letterCombinations("23")
