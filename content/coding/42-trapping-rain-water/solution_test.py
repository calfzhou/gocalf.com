import pytest

from solution import Solution


@pytest.mark.parametrize('height, expected', [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, height, expected):
    assert sol.trap(height) == expected
