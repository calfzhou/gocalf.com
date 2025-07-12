from functools import reduce
import operator


class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        return reduce(operator.xor, derived) == 0
