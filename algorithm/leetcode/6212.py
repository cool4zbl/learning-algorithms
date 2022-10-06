import collections


class Solution:
    def equalFrequency(self, word: str) -> bool:
        dic = {}
        for c in word:
            if dic.get(c) != None:
                dic[c] += 1
            else:
                dic[c] = 1
        print(dic)
        val = dic.values()
        print(i)

        res = [i for i in dic.values() if i != 0]
        return len(res) >= 1


# print(Solution().equalFrequency('abcc'))
# print(Solution().equalFrequency('aazz'))
# print(Solution().equalFrequency('abc'))
# print(Solution().equalFrequency('aaccc'))
print(Solution().equalFrequency('ddaccb'))
