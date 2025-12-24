import pytest

from solution import Solution


def verify(res: str, str1: str, str2: str, expected: str) -> None:
    assert len(res) == len(expected)

    m = len(str1)
    n = len(str2)
    i = j = 0
    for c in res:
        if i < m and str1[i] == c:
            i += 1
        if j < n and str2[j] == c:
            j += 1

    assert i == m
    assert j == n


@pytest.mark.parametrize('str1, str2, expected', [
    ("abac", "cab", "cabac"),
    ("aaaaaaaa", "aaaaaaaa", "aaaaaaaa"),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, str1, str2, expected):
    res = sol.shortestCommonSupersequence(str1, str2)
    if res != expected:
        verify(res, str1, str2, expected)
