import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ('babad', {'bab', 'aba'}),
    ('cbbd', 'bb'),

    ('x', 'x'),
    ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
])
class Test:
    def test_solution(self, s, expected):
        sol = Solution()
        res = sol.longestPalindrome(s)
        if isinstance(expected, str):
            assert res == expected
        else:
            assert res in expected
