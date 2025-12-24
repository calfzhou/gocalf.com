import pytest

from solution import Solution


@pytest.mark.parametrize('s, spaces, expected', [
    ("LeetcodeHelpsMeLearn", [8,13,15], "Leetcode Helps Me Learn"),
    ("icodeinpython", [1,5,7,9], "i code in py thon"),
    ("spacing", [0,1,2,3,4,5,6], " s p a c i n g"),
])
class Test:
    def test_solution(self, s, spaces, expected):
        sol = Solution()
        assert sol.addSpaces(s, spaces) == expected
