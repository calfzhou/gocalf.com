import pytest

from solution import WordDictionary
from solution2 import WordDictionary as WordDictionary2

null = None
true = True
false = False


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
        [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]],
        [null,null,null,null,false,true,true,true]
    ),
])
class Test:
    def test_solution(self, actions, params, expects):
        self._helper(WordDictionary, actions, params, expects)

    def test_solution2(self, actions, params, expects):
        self._helper(WordDictionary2, actions, params, expects)

    def _helper(self, clazz, actions, params, expects):
        d = None
        for action, args, expected in zip(actions, params, expects):
            if action == 'WordDictionary':
                trie = clazz()
            else:
                assert getattr(trie, action)(*args) == expected
