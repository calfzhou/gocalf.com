import pytest

from solution import Solution


@pytest.mark.parametrize('circle1, circle2, expected', [
    ([2, 1, 1], [1, 2, 1], True),
    ([2, 1, 1], [4, 2, 1], False),
])
def test_circles_connected(circle1, circle2, expected):
    sol = Solution()
    assert sol._are_circles_connected(circle1, circle2) == expected


@pytest.mark.parametrize('circle1, circle2, x, y, expected', [
    ([2, 1, 1], [1, 2, 1], 3, 3, True),
    ([2, 1, 1], [1, 2, 1], 2, 2, True),
    ([2, 1, 1], [1, 2, 1], 1, 1, False),
    ([2, 1, 1], [4, 2, 1], 3, 3, False),
    ([2,1000,997], [1000,2,997], 3, 3, False),
    ([22741912, 210810128, 196], [22741920, 210809808,128], 22742157, 210809967, True),
])
def test_circles_connected_inside_rect(circle1, circle2, x, y, expected):
    sol = Solution()
    assert sol._are_circles_connected_inside_rect(circle1, circle2, x, y) == expected


@pytest.mark.parametrize('left, right, y, circle, expected', [
    [0, 3, 0, [2,1,1], True],
    [0, 3, 4, [2,1,1], False],

    [0, 3, 0, [1,1,2], True],
    [0, 3, 3, [1,1,2], True],

    [0, 3, 3, [2,1,1], False],
    [0, 3, 0, [2,1,1], True],
    [0, 3, 3, [1,2,1], True],
    [0, 3, 0, [1,2,1], False],
])
def test_h_line_cross_circle(left, right, y, circle, expected):
    sol = Solution()
    assert sol._is_h_line_cross_circle(left, right, y, circle) == expected


@pytest.mark.parametrize('bottom, top, x, circle, expected', [
    [0, 4, 0, [2,1,1], False],
    [0, 4, 4, [2,1,1], False],

    [0, 3, 0, [1,1,2], True],
    [0, 3, 3, [1,1,2], True],

    [0, 3, 3, [2,1,1], True],
    [0, 3, 0, [2,1,1], False],
    [0, 3, 3, [1,2,1], False],
    [0, 3, 0, [1,2,1], True],
])
def test_v_line_cross_circle(bottom, top, x, circle, expected):
    sol = Solution()
    assert sol._is_v_line_cross_circle(bottom, top, x, circle) == expected


@pytest.mark.parametrize('x, y, circle, expected', [
    [3, 4, [2, 1, 1], (0b0101, False)],
    (3, 3, [1, 1, 2], (0b1111, False)),
    (3, 3, [2, 1, 1], (0b0101, False)),
    (3, 3, [1, 2, 1], (0b1010, False)),
    (4, 4, [5, 5, 1], (0b0000, True)),
    (10, 10, [5, 5, 1], (0b0000, False)),
])
def test_calc_crossed_edges(x, y, circle, expected):
    sol = Solution()
    assert sol._calc_crossed_edges(x, y, circle) == expected
