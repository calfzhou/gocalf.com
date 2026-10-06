import pytest

from solution import MedianFinder
from solution_follow1 import MedianFinder as MedianFinderFollowUp1


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [1], [2], [], [3], []],
        [None, None, None, 1.5, None, 2.0]
    ),
])
class Test:
    def test_solution(self, actions, params, expects):
        self._run(MedianFinder, actions, params, expects)

    def test_solution_follow1(self, actions, params, expects):
        self._run(MedianFinderFollowUp1, actions, params, expects)

    def _run(self, clazz, actions, params, expects):
        finder = None
        for action, args, expected in zip(actions, params, expects):
            if action == 'MedianFinder':
                finder = clazz()
            elif action == 'findMedian':
                assert finder.findMedian(*args) == pytest.approx(expected, abs=1e-5)
            else:
                assert getattr(finder, action)(*args) == expected


@pytest.mark.parametrize('nums, expects', [
    ([1, 2, 3], [1, 1.5, 2]),
    ([2, 3, 4], [2, 2.5, 3]),
    ([4, 2, 3], [4, 3, 3]),
    (
        [42, 37, 38, 50, 71, 5, 65, 12, 93, 71, 25, 55, 95, 4, 67, 18, 72, 36, 25, 17],
        [42, 39.5, 38, 40.0, 42, 40.0, 42, 40.0, 42, 46.0, 42, 46.0, 50, 46.0, 50, 46.0, 50, 46.0, 42, 40.0]
    ),
    (
        [60, 50, 10, 80, 90, 40, 0, 80, 90, 20, 20, 10, 50, 70, 90, 40, 30, 80, 90, 20, 50, 50, 10, 20, 90, 40, 50, 40, 70, 50],
        [60, 55.0, 50, 55.0, 60, 55.0, 50, 55.0, 60, 55.0, 50, 45.0, 50, 50.0, 50, 50.0, 50, 50.0, 50, 50.0, 50, 50.0, 50, 50.0, 50, 50.0, 50, 50.0, 50, 50.0]
    ),
    (
        [0, 50, 50, 100, 100, 0, 0, 100, 100, 0, 50, 0, 0, 100, 0, 0, 100, 0, 50, 0, 100, 50, 0, 50, 0, 50, 100, 0, 100, 100],
        [0, 25.0, 50, 50.0, 50, 50.0, 50, 50.0, 50, 50.0, 50, 50.0, 50, 50.0, 50, 25.0, 50, 25.0, 50, 25.0, 50, 50.0, 50, 50.0, 50, 50.0, 50, 50.0, 50, 50.0]
    ),
])
class TestAll:
    def test_solution(self, nums, expects):
        finder = MedianFinder()
        self._run(finder, nums, expects)

    def test_solution_follow1(self, nums, expects):
        finder = MedianFinderFollowUp1()
        self._run(finder, nums, expects)

    def _run(self, finder, nums, expects):
        for (num, expected) in zip(nums, expects):
            finder.addNum(num)
            assert finder.findMedian() == pytest.approx(expected, abs=1e-5)
