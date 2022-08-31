class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            l
            |
            t   m   m   z   u   x   t
            |
            r
            seen = {t: 0}, l = r =0, max_len = 1

            l
            |
            t   m   m   z   u   x   t
                |
                r
            seen = {t: 0, m: 1}, l = 0, r = 1, max_len = 2
            l
            |
            t   m   m   z   u   x   t
                    |
                    r
            seen = {t: 0, m: 1}, r = 1
                    l
                    |
            t   m   m   z   u   x   t
                    |
                    r
            seen = {t: 0, m: 2}
                    l
                    |
            t   m   m   z   u   x   t
                                |
                                r
            seen = {t: 0, m: 2, z: 3, u: 4, x: 5 }, l = 2, r = 5, max_len = 4
                    l
                    |
            t   m   m   z   u   x   t
                                    |
                                    r
            seen = {t: 0, m: 2, z: 3, u: 4, x: 5 }, l = 2, r = 6
            seen[r] = 0 < l
            seen = {t: 6, m: 2, z: 3, u: 4, x: 5 }, l = 2, r = 6, max_len = 5
        """
        # store elements and their indices
        seen = {}
        l, max_len = 0, 0

        for r, char in enumerate(s):
            # check l <= seen[char] because we don't care [0, seen[char]] now,
            # we start record new substring
            if char in seen and l <= seen[char]:
                l = seen[char] + 1
            else:
                max_len = max(max_len, r - l + 1)

            seen[char] = r
        return max_len