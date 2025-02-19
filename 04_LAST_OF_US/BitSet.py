# https://leetcode.com/problems/design-bitset/

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

# Your Bitset object will be instantiated and called as such:
obj = Bitset(3)
print(f"00 {obj.toString() == '000'}")
obj.fix(0)
print(f"01 {obj.toString() == '100'}")
obj.unfix(1)
print(f"02 {obj.toString() == '100'}")
obj.flip()
print(f"03 {obj.all() == False}")
print(f"04 {obj.one() == True}")
print(f"05 {obj.count() == 2}")
print(f"06 {obj.toString() == '011'}")
