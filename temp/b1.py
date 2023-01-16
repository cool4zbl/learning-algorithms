from typing import List, Tuple, Optional

"""
  Merge HotelRoom object when highPrice + 1 = lowPrice of other object
  Ex.1  [1,2], [3,4] ==> [1,4]
  Ex.2  [1,5],[6,9] ==> [1,9]
  Ex.3 [1,5], [14, 17], [6,9], [10,13] ==> [1,17]
  Ex.3 [1,5], [14, 17], [6,9], [10,13], [4,7], [8,12] ==> [1,17], [4,12]

  union-find ?
  https://leetcode.com/discuss/interview-experience/2401214/Booking.com-or-Backend-Engineer-or-Amsterdam-or-Offer
"""


class Solution:
    def __init__(self):
        self.parent = []

    def findParent(self, node: int):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def setUnion(self, i: int, j: int):
        pi = self.findParent(i)
        pj = self.findParent(j)
        if pi != pj:
            self.parent[pj] = pi

    def merge(self, seq: List[List]):
        res = []
        sz = len(seq)
        self.parent = [i for i in range(sz)]

        for i in range(sz):
            for j in range(sz):
                if seq[j][0] == seq[i][1] + 1:
                    self.setUnion(i, j)
        k = 0
        while k < sz:
            mini, maxi = seq[k][0], seq[k][1]
            while k + 1 < sz and self.parent[k] == self.parent[k+1]:
                k += 1
                mini = min(mini, seq[k][0])
                maxi = max(maxi, seq[k][1])
            res.append([mini, maxi])
            k += 1

        return res


t1 = [[1, 2], [3, 4]]
t2 = [[1, 5], [6, 9]]
t3 = [[1, 5], [14, 17], [6, 9], [10, 13]]
t4 = [[1, 5], [14, 17], [6, 9], [10, 13], [4, 7], [8, 12]]
print(Solution().merge(t1))
print(Solution().merge(t2))
print(Solution().merge(t3))
print(Solution().merge(t4))
