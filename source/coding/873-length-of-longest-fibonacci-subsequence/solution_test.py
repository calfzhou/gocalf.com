import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('arr, expected', [
    ([1,2,3,4,5,6,7,8], 5),
    ([1,3,7,11,12,14,18], 3),

    ([1,3,5], 0),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, arr, expected):
    assert sol.lenLongestFibSubseq(arr) == expected
