from typing import List, Tuple, Optional
from collections import defaultdict, Counter


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        vis = [False] * numCourses

        for v1, v2 in prerequisites:
            graph[v1].append(v2)

        def dfs(cur):
            for v in graph[cur]:
                if vis[v]:
                    return False
                vis[v] = True
                if not dfs(v):
                    return False
            return True

        for i in range(numCourses):
            if not vis[i] and not dfs(i):
                return False
        return True
