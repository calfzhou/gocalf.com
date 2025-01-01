import pytest

from solution import Solution


def verify(res, s):
    assert sorted(res) == sorted(s)
    prev = res[0]
    for i in range(1, len(s)):
        assert prev != res[i]
        prev = res[i]


@pytest.mark.parametrize('s, expected', [
    ("aab", "aba"),
    ("aaab", ""),

    ("vvvlo", "vlvov"),
    ("aabbcc", "abacbc"),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, expected):
    res = sol.reorganizeString(s)
    if expected == '':
        assert res == ''
    else:
        assert res != ''
        if res != expected:
            verify(res, s)
