import pytest

from solution import Solution


@pytest.mark.parametrize('s, k, expected', [
    ("aaabcccd", 2, 4),
    ("aabbaa", 2, 2),
    ("aaaaaaaaaaa", 0, 3),

    ("a", 1, 0),
    ("babbab", 5, 1),
    ("aabaabbcbbbaccc", 6, 4),
    ("abcdefghijklmnopqrstuvwxyz", 16, 10),
])
class Test:
    def test_solution(self, s, k, expected):
        sol = Solution()
        assert sol.getLengthOfOptimalCompression(s, k) == expected
