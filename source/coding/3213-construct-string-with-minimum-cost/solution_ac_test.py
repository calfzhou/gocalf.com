import pytest

from solution import TrieTree


@pytest.mark.parametrize('target, words, costs, expected', [
    ("hello worldhello", ["hello", "world"], [1, 2], [(0,0+5,1), (6,6+5,2), (11,11+5,1)]),
    ("abxabcabcaby", ["ab", "abc", "aby"], [1, 2, 3], [(0,0+2,1), (3,3+2,1), (3,3+3,2), (6,6+2,1), (6,6+3,2), (9,9+2,1), (9,9+3,3)]),

    ("abcdef", ["abdef","abc","d","def","ef"], [100,1,1,10,5], [(0,0+3,1), (3,3+1,1), (3,3+3,10), (4,4+2,5)]),
    ("aaaa", ["z","zz","zzz"], [1,10,100], []),

    ("r", ["r","r","r","r"], [1,6,3,3], [(0,1,1)]),
])
class Test:
    def test_solution(self, target, words, costs, expected):
        trie = TrieTree()
        for word, cost in zip(words, costs): trie.add(word, cost)
        trie.build_ac()
        matches = list(trie.match(target))
        assert matches == expected
