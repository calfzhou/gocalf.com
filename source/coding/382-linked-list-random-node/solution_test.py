import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.linked_list import build_linked_list
from solution import Solution
from solution2 import Solution as Solution2

null = None


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"],
        [[[1, 2, 3]], [], [], [], [], []],
        [null, 1, 3, 2, 2, 3],
    ),
])
@pytest.mark.parametrize('clazz', [Solution, Solution2])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'Solution':
            nums = args[0]
            sol = clazz(build_linked_list(nums))
        elif action == 'getRandom':
            res = getattr(sol, action)(*args)
            if res != expected:
                assert res in nums
        else:
            assert getattr(sol, action)(*args) == expected

