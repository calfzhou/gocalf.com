import pytest

from solution import Solution


@pytest.mark.parametrize('words, target, expected', [
    (["acca","bbbb","caca"], "aba", 6),
    (["abba","baab"], "bab", 4),

    (
        ["cbabddddbc","addbaacbbd","cccbacdccd","cdcaccacac","dddbacabbd","bdbdadbccb","ddadbacddd","bbccdddadd","dcabaccbbd","ddddcddadc","bdcaaaabdd","adacdcdcdd","cbaaadbdbb","bccbabcbab","accbdccadd","dcccaaddbc","cccccacabd","acacdbcbbc","dbbdbaccca","bdbddbddda","daabadbacb","baccdbaada","ccbabaabcb","dcaabccbbb","bcadddaacc","acddbbdccb","adbddbadab","dbbcdcbcdd","ddbabbadbb","bccbcbbbab","dabbbdbbcb","dacdabadbb","addcbbabab","bcbbccadda","abbcacadac","ccdadcaada","bcacdbccdb"],
        "bcbbcccc",
        677452090
    ),
    (["abba","baab"], "babbbb", 0),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, words, target, expected):
    assert sol.numWays(words, target) == expected
