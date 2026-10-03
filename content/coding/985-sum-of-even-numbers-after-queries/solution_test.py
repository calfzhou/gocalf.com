import pytest

from solution import Solution


@pytest.mark.parametrize('nums, queries, expected', [
    ([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]], [8,6,2,4]),
    ([1], [[4,0]], [0]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, queries, expected):
    assert sol.sumEvenAfterQueries(nums.copy(), queries) == expected
