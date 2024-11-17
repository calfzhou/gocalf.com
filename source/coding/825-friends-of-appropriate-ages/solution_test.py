import pytest

from solution import Solution

@pytest.mark.parametrize('ages, expected', [
    ([16,16], 2),
    ([16,17,18], 2),
    ([20,30,100,110,120], 3),
])
class Test:
    def test_solution(self, ages, expected):
        sol = Solution()
        assert sol.numFriendRequests(ages) == expected
