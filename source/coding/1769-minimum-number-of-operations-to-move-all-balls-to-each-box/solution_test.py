import pytest

from solution import Solution


@pytest.mark.parametrize('boxes, expected', [
    ("110", [1,1,3]),
    ("001011", [11,8,5,4,3,4]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, boxes, expected):
    assert sol.minOperations(boxes) == expected
