import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('s, wordDict, expected', [
    ("leetcode", ["leet","code"], True),
    ("applepenapple", ["apple","pen"], True),
    ("catsandog", ["cats","dog","sand","and","cat"], False),
])
class Test:
    def test_solution(self, s, wordDict, expected):
        sol = Solution()
        assert sol.wordBreak(s, wordDict) == expected

    def test_solution2(self, s, wordDict, expected):
        sol = Solution2()
        assert sol.wordBreak(s, wordDict) == expected
