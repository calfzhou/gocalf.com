import pytest

from solution import Solution


@pytest.mark.parametrize('sentence, searchWord, expected', [
    ("i love eating burger", "burg", 4),
    ("this problem is an easy problem", "pro", 2),
    ("i am tired", "you", -1),

    ("i love eating burger", "eating", 3),
    ("i love eating burger", "seeing", -1),
    ("i love eating burger", "g", -1),
    ("i love eating burger", "eats", -1),
])
class Test:
    def test_solution(self, sentence, searchWord, expected):
        sol = Solution()
        assert sol.isPrefixOfWord(sentence, searchWord) == expected
