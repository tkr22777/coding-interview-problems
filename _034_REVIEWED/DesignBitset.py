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