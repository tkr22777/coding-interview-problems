"""
Problem Summary:
Design a Bitset data structure that manages a fixed-size sequence of bits (0s and 1s).
The Bitset class should support the following operations:
- Initialize with a specific size, setting all bits to 0
- Fix a bit at a specific index (set to 1)
- Unfix a bit at a specific index (set to 0)
- Flip all bits (0s become 1s, and 1s become 0s)
- Check if all bits are set to 1
- Check if at least one bit is set to 1
- Count the number of bits set to 1
- Convert the bitset to a string representation

This implementation uses two sets to track the indices of 0s and 1s,
providing efficient operations for all required functionalities.
"""

class Bitset:
    def __init__(self, size: int):
        self.size = size
        self.ones = set()
        self.zeros = set()
        for i in range(size):
            self.zeros.add(i)

    def fix(self, idx: int) -> None:
        self.ones.add(idx)
        if idx in self.zeros:
            self.zeros.remove(idx)

    def unfix(self, idx: int) -> None:
        self.zeros.add(idx)
        if idx in self.ones:
            self.ones.remove(idx)

    def flip(self) -> None:
        self.zeros, self.ones = self.ones, self.zeros

    def all(self) -> bool:
        return len(self.ones) == self.size

    def one(self) -> bool:
        return len(self.ones) > 0

    def count(self) -> int:
        return len(self.ones)

    def toString(self) -> str:
        out = []
        for i in range(self.size):
            if i in self.ones:
                out.append("1")
            else:
                out.append("0")
        return "".join(out)

# Test cases
obj = Bitset(3)
obj.fix(0)
obj.unfix(1)
obj.flip()
param_4 = obj.all()
param_5 = obj.one()
param_6 = obj.count()
param_7 = obj.toString()
print(param_4)
print(param_5)
print(str(param_6))
print(param_7) 