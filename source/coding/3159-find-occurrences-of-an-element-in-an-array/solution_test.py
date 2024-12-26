import pytest

from solution import Solution


@pytest.mark.parametrize('nums, queries, x, expected', [
    ([1,3,1,7], [1,3,2,4], 1, [0,-1,2,-1]),
    ([1,2,3], [10], 5, [-1]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, queries, x, expected):
    assert sol.occurrencesOfElement(nums, queries, x) == expected
