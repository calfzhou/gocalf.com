from typing import Counter
import pytest

from solution import Solution


@pytest.mark.parametrize('n, expected', [
    (4, "pppz"),
    (2, "xy"),
    (7, "holasss"),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, n, expected):
    res = sol.generateTheString(n)
    if res != expected:
        assert len(res) == n
        counts = Counter(res)
        remains = [freq & 1 for freq in counts.values()]
        assert remains == [1] * len(counts)
