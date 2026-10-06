import pytest

from solution import Solution
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3


@pytest.mark.parametrize('arr, expected', [
    ([1,-2,0,3], 4),
    ([1,-2,-2,3], 3),
    ([-1,-1,-1,-1], -1),

    ([-2,1,-3,4,-1,2,1,-5,4], 10),
    ([1], 1),
    ([5,4,-1,7,8], 24),
    ([-3,2,-2,-1,3,-2,3], 6),
    ([1,2,3,4], 10),

    ([-50], -50),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2(), Solution3()])
def test_solution(sol, arr, expected):
    assert sol.maximumSum(arr) == expected
