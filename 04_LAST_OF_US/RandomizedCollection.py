
from collections import defaultdict, deque
import random


class RandomizedCollection:

    def __init__(self):
        self.map = defaultdict(set)
        self.list = []

    def insert(self, val: int) -> bool:
        self.list.append(val)
        self.map[val].add(len(self.list))
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        # if the size of the list is 1:
        indices = self.map[val]

        if self.list[len(self.list) - 1] == val:
            indices.remove(len(self.list) - 1)
            self.list.pop()
            if len(indices) == 0:
                del self.map[val]
            return True

        index = indices.pop()
        if len(indices) == 0:
            del self.map[val]

        val_mv_i = len(self.list) - 1
        val_mv = self.list.pop()
        self.list[index] = val_mv
        self.map[val_mv].remove(val_mv_i)
        self.map[val_mv].add(index)
        return True

    def getRandom(self) -> int:
        i = random.randint(0, len(self.list) - 1)
        return self.list[i]


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.getRandom()


# let's store in a list
# keep a mapping to the index of the elem for deletion

# why don't I use a linked hash map?
# LHM: add -> O(1) // would replace for duplicate wouldn't work
# LHM: remove -> O(1)  
# LHM 
