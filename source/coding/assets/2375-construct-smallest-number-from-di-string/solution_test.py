import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('pattern, expected', [
    ("IIIDIDDD", "123549876"),
    ("DDD", "4321"),

    ("IDID", "13254"),
    ("IIDDID", "1254376"),
    ("IDDIID", "1432576"),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, pattern, expected):
    assert sol.smallestNumber(pattern) == expected
