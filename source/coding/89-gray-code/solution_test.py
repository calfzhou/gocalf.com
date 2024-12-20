import pytest

from solution import Solution


# 191-number-of-1-bits#Another-Way
def hamming_weight(n: int) -> int:
    cnt = 0
    while n > 0:
        cnt += 1
        n &= n - 1

    return cnt


def validate_gray_code(nums: list[int]) -> None:
    n = len(nums)
    assert sorted(nums) == list(range(n))
    assert nums[0] == 0
    for i in range(len(nums)):
        assert hamming_weight(nums[i-1] ^ nums[i]) == 1


@pytest.mark.parametrize('n, expected', [
    (2, [0,1,3,2]),
    (1, [0,1]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, n, expected):
    result = sol.grayCode(n)
    if result != expected:
        assert len(result) == 2 ** n
        validate_gray_code(result)
