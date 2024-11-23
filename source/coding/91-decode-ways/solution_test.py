import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("12", 2),
    ("226", 3),
    ("06", 0),

    ("11106", 2),
])
class Test:
    def test_solution(self, s, expected):
        sol = Solution()
        assert sol.numDecodings(s) == expected
