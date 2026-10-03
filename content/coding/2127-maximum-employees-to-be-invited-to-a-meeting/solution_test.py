import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('favorite, expected', [
    ([2,2,1,2], 3),
    ([1,2,0], 3),
    ([3,0,1,4,1], 4),

    ([1,0,0,2,1,4,7,8,9,6,7,10,8], 6),
    ([1,0,3,2,5,6,7,4,9,8,11,10,11,12,10], 11)
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, favorite, expected):
    assert sol.maximumInvitations(favorite) == expected
