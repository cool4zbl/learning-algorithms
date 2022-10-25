from typing import List, Tuple, Optional


class UF:
    def __init__(self, n) -> None:
        self.parent = list(range(n+1))

    def union(self, p: int, q: int):
        self.parent[self.find(p)] = self.find(q)

    def isConnected(self, p: int, q: int):
        return self.parent[self.find(p)] == self.parent[self.find(q)]

    def find(self, p: int):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UF(n)

        for v1, v2 in edges:
            if uf.isConnected(v1, v2):
                return [v1, v2]
            uf.union(v1, v2)
        return [-1, -1]


edges = [[1, 2], [1, 3], [2, 3]]
print(Solution().findRedundantConnection(edges))
