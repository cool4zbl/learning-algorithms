from typing import List


class Solution:

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for i in range(31):
            ones_a = ones_b = 0
            for a in nums1:
                if a & (1 << i):
                    ones_a += 1
            for b in nums2:
                if b & (1 << i):
                    ones_b += 1
            if ones_a * ones_b & 1:
                ans |= 1 << i
        return ans

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = [n1 ^ n2 for n1 in nums1 for n2 in nums2]
        print(res)

        xor_pre = [0] * (len(res) + 1)
        xor_pre[0] = res[0]
        for i in range(len(res)):
            xor_pre[i] = xor_pre[i-1] ^ res[i]

        print(xor_pre)

        n = len(res)

        return xor_pre[n] ^ xor_pre[0]


# nums1 = [2, 1, 3]
# nums2 = [10, 2, 5, 0]
# print(Solution().xorAllNums(nums1, nums2))
nums1 = [1, 2]
nums2 = [3, 4]
print(Solution().xorAllNums(nums1, nums2))
