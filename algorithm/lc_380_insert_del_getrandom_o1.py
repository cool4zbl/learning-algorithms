import random
class RandomizedSet:

    def __init__(self):
        self.cache = {}
        self.arr = [] # kind of like database

    def insert(self, val: int) -> bool:
        if val in self.cache:
            return False

        """
            write db first, then write cache.
        """
        self.arr.append(val)
        self.cache[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.cache:
            return False

        """
        Notice:
        0. update the index of the last = arr[-1] in cache first
        1. swap a[index], a[-1]
        2. arr.pop()
        3. del cache[val]
        """
        arr = self.arr
        index = self.cache[val]

        # update cache val
        self.cache[arr[-1]] = index

        # delete in db
        arr[index], arr[-1] = arr[-1], arr[index]
        arr.pop()

        # delete cache
        del self.cache[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()