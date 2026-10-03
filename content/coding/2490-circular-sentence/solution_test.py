import pytest

from solution import Solution


@pytest.mark.parametrize('sentence, expected', [
    ("leetcode exercises sound delightful", True),
    ("eetcode", True),
    ("Leetcode is cool", False),
])
class Test:
    def test_solution(self, sentence, expected):
        sol = Solution()
        assert sol.isCircularSentence(sentence) == expected
