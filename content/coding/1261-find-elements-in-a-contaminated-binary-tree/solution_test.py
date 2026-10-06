import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import build_tree
from solution import FindElements
from solution2 import FindElements as FindElements2

null = None
false = False
true = True


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["FindElements","find","find"],
        [[[-1,null,-1]],[1],[2]],
        [null,false,true],
    ),
    (
        ["FindElements","find","find","find"],
        [[[-1,-1,-1,-1,-1]],[1],[3],[5]],
        [null,true,true,false],
    ),
    (
        ["FindElements","find","find","find","find"],
        [[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]],
        [null,true,false,false,true],
    ),
])
@pytest.mark.parametrize('clazz', [FindElements, FindElements2])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'FindElements':
            sol = clazz(build_tree(args[0]))
        else:
            assert getattr(sol, action)(*args) == expected
