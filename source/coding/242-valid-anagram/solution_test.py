import pytest

from solution import Solution


@pytest.mark.parametrize('s, t, expected', [
    ("anagram", "nagaram", True),
    ("rat", "cat", False),
])
class Test:
    def test_solution(self, s, t, expected):
        sol = Solution()
        assert sol.isAnagram(s, t) == expected
