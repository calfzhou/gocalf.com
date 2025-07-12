import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('s, numOps, expected', [
    ("000001", 1, 2),
    ("0000", 2, 1),
    ("0101", 0, 1),

    ("000", 0, 3),
    ("00011", 1, 2),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, s, numOps, expected):
    assert sol.minLength(s, numOps) == expected
