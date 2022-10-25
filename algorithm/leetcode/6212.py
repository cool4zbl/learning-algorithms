import collections


class Solution:
    def equalFrequency(self, word: str) -> bool:
        dic = {}
        for c in word:
            if dic.get(c) != None:
                dic[c] += 1
            else:
                dic[c] = 1

        res = [i for i in dic.values() if i != 0]
        return len(res) >= 1


print(Solution().equalFrequency('ddaccb'))
