import pytest

from solution import Solution


def _sort(groups: list[list[int]]):
    for group in groups:
        group.sort()

    groups.sort()

@pytest.mark.parametrize('strs, expected', [
    (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
    ([''], [['']]),
    (['a'], [['a']]),
])
class Test:
    def test_solution(self, strs, expected):
        sol = Solution()
        result = sol.groupAnagrams(strs)
        _sort(result)
        _sort(expected)
        assert result == expected
