import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
    ([0], [[],[0]]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    res = sol.subsets(nums)
    res = [sorted(x) for x in res]
    res.sort()
    expected = [sorted(x) for x in expected]
    expected.sort()
    assert res == expected
