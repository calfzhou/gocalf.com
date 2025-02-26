import pytest

from solution import Solution
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3


@pytest.mark.parametrize('arr, expected', [
    ([1,3,5], 4),
    ([2,4,6], 0),
    ([1,2,3,4,5,6,7], 16),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2(), Solution3()])
def test_solution(sol, arr, expected):
    assert sol.numOfSubarrays(arr) == expected
