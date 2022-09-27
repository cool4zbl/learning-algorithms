from typing import List


def temperatureTrend(tempA: List[int], tempB: List[int]) -> int:
    ans, cur = 0, 0

    for i in range(1, len(tempA)):
        tA = (tempA[i] > tempA[i-1]) - (tempA[i] < tempA[i - 1])
        tB = (tempB[i] > tempB[i-1]) - (tempB[i] < tempB[i - 1])
        if tA - tB == 0:
            cur += 1
            ans = max(ans, cur)
        else:
            cur = 0

    return ans


t1 = [21, 18, 18, 18, 31]
t2 = [34, 32, 16, 16, 17]
print(temperatureTrend(t1, t2))
