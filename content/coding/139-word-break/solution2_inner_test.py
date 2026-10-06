import pytest

from solution2 import TrieTree


@pytest.mark.parametrize('words, text, start, expected', [
    (['code', 'leet'], 'leetcode', 0, ['leet']),
    (['code', 'leet'], 'lee', 0, []),
    (['code', 'leet'], 'leet', 0, ['leet']),
    (['code', 'leet'], 'leetcode', 4, ['code']),
    (['dog', 'dogs'], 'dogsandcat', 0, ['dog', 'dogs']),
    (['', 'dog', 'dogs', 'cat'], 'dogsandcat', 0, ['', 'dog', 'dogs']),
])
class Test:
    def test_trie_lookup(self, words, text, start, expected):
        tree = TrieTree(words)
        positions = list(tree.lookup(text, start))
        result = [text[start:p] for p in positions]
        assert result == expected
