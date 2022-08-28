def twoSum(nums, target):
    d = {}
    l = []
    for i, n in enumerate(nums):
        val = target - n
        if d.get(val) != None:
            return [d.get(val), i]
        d[n] = i
    return []

s = twoSum([2,7,11,3], 9)
print(s)