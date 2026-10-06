class ProductOfNumbers:

    def __init__(self):
        self._products: list[int] = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self._products = [1]
        else:
            self._products.append(self._products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self._products):
            return 0
        else:
            return self._products[-1] // self._products[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
