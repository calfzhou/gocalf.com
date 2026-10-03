import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('arr, expected', [
    ([10,2,5,3], True),
    ([3,1,7,11], False),

    ([-2,0,10,-19,4,6,-8], False),
    ([0,0], True),
])
class Test:
    def test_solution(self, arr, expected):
        sol = Solution()
        assert sol.checkIfExist(arr) == expected

    def test_solution2(self, arr, expected):
        sol = Solution2()
        assert sol.checkIfExist(arr) == expected
