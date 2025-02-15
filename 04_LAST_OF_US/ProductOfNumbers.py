class ProductOfNumbers:

    def __init__(self):
        self.data = []
        self.last_zero = -1

    def add(self, num: int) -> None:
        if num > 1:
            for i in range(self.last_zero + 1, len(self.data)):
                self.data[i] *= num

        self.data.append(num)

        if num == 0:
            self.last_zero = len(self.data) - 1

    def getProduct(self, k: int) -> int:
        # k = 1, n - 1 - (k - 1)
        # k = 2, n - 1 - (2 - 1), n - 2
        # k = 3, n - 1 - (3 - 1), n - 3
        index = len(self.data) - 1 - (k - 1)
        if index > self.last_zero:
            return self.data[index]
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

productOfNumbers = ProductOfNumbers();
productOfNumbers.add(3);
productOfNumbers.add(0);
productOfNumbers.add(2);
productOfNumbers.add(5);
productOfNumbers.add(4);
print(productOfNumbers.getProduct(2) == 20)
print(productOfNumbers.getProduct(3) == 40)
print(productOfNumbers.getProduct(4) == 0)
productOfNumbers.add(8);
print(productOfNumbers.getProduct(2) == 32)
