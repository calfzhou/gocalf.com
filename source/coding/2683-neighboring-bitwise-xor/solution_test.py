import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('derived, expected', [
    ([1,1,0], True),
    ([1,1], True),
    ([1,0], False),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, derived, expected):
    assert sol.doesValidArrayExist(derived) == expected
