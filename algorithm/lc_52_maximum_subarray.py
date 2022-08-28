import sys
# solution1 Time O(n), Space O(n)
# 如果不需要返回具体是什么数组，其实无需记忆每次算出来的 sum
def maxSubArray(nums) -> int:
    if len(nums) == 1:
        return nums[0]

    preSum = [0]
    for i in range(len(nums)):
        preSum.append(nums[i] + preSum[i])

    re = -sys.maxsize-1
    minSum = sys.maxsize
    for i in range(len(nums)):
        minSum = min(minSum, preSum[i])
        # KEY POINT: the maximum subarray
        re = max(re, preSum[i + 1] - minSum)

    return re

# solution2


# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([-2, -1]))
# print(maxSubArray([1]))
# print(maxSubArray([5,4,-1,7,8]))
# print(maxSubArray([-1, 1, 0, -2]))
# print(maxSubArray([1,1,1]))
# print(maxSubArray([2, -2, 0, 1, -1]))