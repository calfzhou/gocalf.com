import pytest

from solution_ac import TrieTree


@pytest.mark.parametrize('target, words, expected', [
    ("hello worldhello", ["hello", "world"], [(0,0+5), (6,6+5), (11,11+5)]),
    ("abxabcabcaby", ["ab", "abc", "aby"], [(0,0+2), (3,3+3), (6,6+3), (9,9+3)]),
    ("abcdef", ["abdef","abc","d","def","ef"], [(0,0+3), (3,3+3)]),
    ("aaaa", ["z","zz","zzz"], []),
    ("r", ["r"], [(0,1)]),

    ("aabcdabc", ["abc","aaaaa","bcdef"], [(0,2), (1,1+2,1+3), (2,2+3,2+3), (5,5+3)]),
    ("ababaababa", ["abababab","ab"], [(0,5), (5,5+5)]),
    ("xyz", ["abcdef"], []),
    ("aacaacbabb", ["caacbbbbbcaccbcbcccbcbbbcbcabbcaaacabbcbbccabcac","baccccb","aacabcca"], [(0,4), (2,2+3,2+5), (6,6+2,6+2), (8,8+1), (9,9+1)]),
    ("beeea", ["adaeabcabdcaabbeceeadeaebcdddeadcbceeeadddabdc","a"], [(4,4+1)]),
])
class Test:
    def test_ac(self, target, words, expected):
        trie = TrieTree()
        for word in words: trie.add(word)
        trie.build_ac()
        matches = list(trie.prefix(target))
        expected = self._expand_pieces(expected)
        assert matches == expected

    def _expand_pieces(self, pieces):
        result = []
        # for i, j in pieces:
        #     result.extend((i, k+1) for k in range(i, j))
        for piece in pieces:
            if len(piece) == 3:
                i, j1, j = piece
            else:
                i, j = piece
                j1 = i + 1
            result.extend((i, k) for k in range(j1, j + 1))

        return result
