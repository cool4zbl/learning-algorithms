from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        time = [0] * n

        for i in range(len(logs)):
            id, cur_time = logs[i]
            t = cur_time - (logs[i - 1][1] if i > 0 else 0)
            if time[id] < t:
                time[id] = t
            # print(id, time[id])

        idx = time.index(max(time))
        return idx


n = 10
logs = [[0, 3], [2, 5], [0, 9], [1, 15]]
print(Solution().hardestWorker(n, logs))
n = 26
logs = [[1, 1], [3, 7], [2, 12], [7, 17]]
print(Solution().hardestWorker(n, logs))
n = 2
logs = [[0, 10], [1, 20]]
print(Solution().hardestWorker(n, logs))
n = 450
logs = [[110, 5], [360, 7], [48, 8], [
    286, 10], [167, 12], [110, 13], [221, 18]]
print(Solution().hardestWorker(n, logs))
