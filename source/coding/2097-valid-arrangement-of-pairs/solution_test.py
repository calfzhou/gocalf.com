import itertools
import pytest

from solution import Solution


@pytest.mark.parametrize('pairs, expected', [
    ([[5,1],[4,5],[11,9],[9,4]], [[11,9],[9,4],[4,5],[5,1]]),
    ([[1,3],[3,2],[2,1]], [[1,3],[3,2],[2,1]]),
    ([[1,2],[1,3],[2,1]], [[1,2],[2,1],[1,3]]),

    (
        [[5,13],[10,6],[11,3],[15,19],[16,19],[1,10],[19,11],[4,16],[19,9],[5,11],[5,6],[13,5],[13,9],[9,15],[11,16],[6,9],[9,13],[3,1],[16,5],[6,5]],
        [[4,16],[16,5],[5,6],[6,5],[5,11],[11,16],[16,19],[19,9],[9,13],[13,5],[5,13],[13,9],[9,15],[15,19],[19,11],[11,3],[3,1],[1,10],[10,6],[6,9]]
    ),
])
class Test:
    def test_solution(self, pairs, expected):
        sol = Solution()
        result = sol.validArrangement(pairs.copy())
        assert sorted(result) == sorted(pairs)
        assert self._is_valid(result)

    def _is_valid(self, pairs):
        for a, b in itertools.pairwise(pairs):
            if a[1] != b[0]:
                return False

        return True
