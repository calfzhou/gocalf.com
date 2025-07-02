import pytest

from solution import Solution


@pytest.mark.parametrize('chars, expected, result', [
    (["a","a","b","b","c","c","c"], 6, ["a","2","b","2","c","3"]),
    (["a"], 1, ["a"]),
    (["a","b","b","b","b","b","b","b","b","b","b","b","b"], 4, ["a","b","1","2"]),
])
class Test:
    def test_solution(self, chars, expected, result):
        sol = Solution()
        chars = chars.copy()
        assert sol.compress(chars) == expected
        assert chars == result
