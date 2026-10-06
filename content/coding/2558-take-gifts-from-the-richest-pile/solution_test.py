import pytest

from solution import Solution


@pytest.mark.parametrize('gifts, k, expected', [
    ([25,64,9,4,100], 4, 29),
    ([1,1,1,1], 4, 4),
])
class Test:
    def test_solution(self, gifts, k, expected):
        sol = Solution()
        assert sol.pickGifts(gifts.copy(), k) == expected
