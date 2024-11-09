import pytest

from solution import NeighborSum


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["NeighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"],
        [[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]],
        [None, 6, 16, 16, 4],
    ),
    (
        ["NeighborSum", "adjacentSum", "diagonalSum"],
        [[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]]], [15], [9]],
        [None, 23, 45],
    ),
])
def test_neighbor_sum(actions, params, expects):
    ns = None
    for action, param, expected in zip(actions, params, expects):
        if action == 'NeighborSum':
            ns = NeighborSum(*param)
        elif action == 'adjacentSum':
            assert ns.adjacentSum(*param) == expected
        elif action == 'diagonalSum':
            assert ns.diagonalSum(*param) == expected
