from typing import List
import collections


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums.append(int(str(nums[i])[::-1]))
        c = collections.Counter(nums)
        return len(c.keys())

    def sumOfNumberAndReverse(self, num: int) -> bool:
        n = 1
        while n < num:
            r = int(str(n)[::-1])
            if r + n == num:
                return True
            n += 1
        return False

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def subArray(arr, n):
            count = 0
            res = []
            # for i in range(0, n):
            i = 0
            while i < n:
                for j in range(i, n):
                    d = [1e7, 0]
                    c = []
                    for k in range(i, j+1):
                        if arr[k] > d[1]:
                            d[1] = arr[k]
                        if arr[k] < d[0]:
                            d[0] = arr[k]
                        c.append(arr[k])
                        print('d', d)
                        if d[1] > maxK:
                            break
                        if d[0] < minK:
                            break

                    if d[0] == minK and d[1] == maxK:
                        res.append(c)
                    # if d[0] > minK and d[1]:
                    #     i = j
                    # if d[1] < maxK:
                    #     continue
                i += 1

            print(res)

            return len(res)

        return subArray(nums, len(nums))

        # deq = collections.deque()
        # res = subArray(nums, len(nums))

        # for r in res:
        #     if min(r) == minK and max(r) == maxK:
        #         count += 1

        # return count


# Solution().countDistinctIntegers([1, 13, 10, 12, 31])
n1 = [1, 3, 5, 2, 7, 5]
n2 = [1, 1, 1, 1]
print(Solution().countSubarrays(n1, 1, 5))
# print(Solution().countSubarrays(n2, 1, 1))
