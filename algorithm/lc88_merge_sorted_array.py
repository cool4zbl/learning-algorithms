class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
            The point is how we confirm the order of numbers.
            Since the two arrays are already in non-decreasing order, we can place two pointers at the end of each array, the `m-1` index of nums1 and the `n-1` index of nums2.
            Each time, we copy the larger num to the end of nums1 and then move it forward one pos.
            Because we also want to locate the end of nums1, we also need a third pointer for copying.

            In the following, we directly use `m` and `n` as pointers to the two arrays, and create an additional `pos` pointer starting at `m+n-1`.
            Each time we move `m` or `n` forward, we also move `pos` forward.

            Note that if the numbers of nums1 have been copied, do not forget to continue copying the numbers of nums2;
            If numbers of nums2 have been copied, the remaining numbers of nums1 don't need to be changed, as they are already in order.

        """
        i = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1

        while n >= 0:
            nums1[i] = nums2[n]
            n -= 1
            i -= 1
