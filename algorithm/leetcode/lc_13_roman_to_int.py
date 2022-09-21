"""
    https://leetcode.com/problems/roman-to-integer/
    @20220725
    remember, use a len+1 arr to compare and calculate the sum
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        """
            >>>
                s = Solution()
                s.romanToInt("III3")
        """
        r_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        arr = []

        for c in list(s):
            try:
                n = r_map[c]
                arr.append(n)
            except Exception as ex:
                print("err", ex, c)

        arr.append(0)

        result = 0
        for i in range(len(arr) - 1):
            result += arr[i] if arr[i] >= arr[i+1] else (-arr[i])

        return result
