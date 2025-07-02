import pytest

from solution import Solution


@pytest.mark.parametrize('candidates, expected', [
    ([16,17,71,62,12,24,14], 4),
    ([8,8], 2),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, candidates, expected):
    assert sol.largestCombination(candidates) == expected
