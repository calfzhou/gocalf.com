import pytest

from solution import Trie


null = None
true = True
false = False


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
        [null, null, true, false, true, null, true]
    ),
    (
        ["Trie","search"],
        [[],["a"]],
        [null,false]
    ),
])
class Test:
    def test_solution(self, actions, params, expects):
        trie = None
        for action, args, expected in zip(actions, params, expects):
            if action == 'Trie':
                trie = Trie()
            else:
                assert getattr(trie, action)(*args) == expected
