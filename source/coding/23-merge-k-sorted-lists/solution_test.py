import pytest

from node import ListNode
from solution import Solution


@pytest.mark.parametrize('lists, expected', [
    ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ([], []),
    ([[]], []),

    (
        [
            [55, 197, 202, 272, 456, 514, 529, 838, 888, 890, 918, 996],
            [133, 272, 387, 431, 522, 729, 770, 817, 900, 902],
            [35, 100, 175, 324, 416, 439, 658, 824, 886, 989],
            [15, 57, 108, 127, 189, 313, 405, 489, 499, 516, 608, 628, 687, 742, 853, 925],
            [111, 132, 209, 244, 264, 291, 317, 380, 470, 481, 490, 635, 688, 889, 946, 986],
            [76, 83, 332, 427, 596, 612, 660, 673, 764, 844, 964, 978, 997, 999],
            [5, 18, 146, 244, 344, 402, 420, 470, 549, 686, 697, 708, 768, 778, 802, 876],
            [58, 153, 290, 352, 386, 535, 638, 777, 826, 829, 852, 894, 937, 947],
            [190, 192, 367, 426, 453, 469, 563, 594, 654, 699, 792, 828, 857, 942, 960, 992, 1000],
            [3, 94, 115, 175, 393, 400, 423, 465, 521, 526, 674, 844, 872, 885, 919],
        ],
        [
            3, 5, 15, 18, 35, 55, 57, 58, 76, 83, 94, 100, 108, 111, 115, 127, 132, 133, 146, 153, 175, 175, 189, 190,
            192, 197, 202, 209, 244, 244, 264, 272, 272, 290, 291, 313, 317, 324, 332, 344, 352, 367, 380, 386, 387,
            393, 400, 402, 405, 416, 420, 423, 426, 427, 431, 439, 453, 456, 465, 469, 470, 470, 481, 489, 490, 499,
            514, 516, 521, 522, 526, 529, 535, 549, 563, 594, 596, 608, 612, 628, 635, 638, 654, 658, 660, 673, 674,
            686, 687, 688, 697, 699, 708, 729, 742, 764, 768, 770, 777, 778, 792, 802, 817, 824, 826, 828, 829, 838,
            844, 844, 852, 853, 857, 872, 876, 885, 886, 888, 889, 890, 894, 900, 902, 918, 919, 925, 937, 942, 946,
            947, 960, 964, 978, 986, 989, 992, 996, 997, 999, 1000,
        ]
    ),
    (
        [
            [5, 7, 10, 24, 29, 32, 34, 35, 35, 43, 53, 55, 55, 58, 69, 89, 92, 94, 100],
            [0, 1, 4, 6, 7, 8, 14, 29, 31, 42, 45, 56, 73, 74, 75, 79, 79, 86, 92, 100],
            [0, 2, 25, 28, 33, 37, 44, 51, 58, 69, 72, 73, 77, 81, 84, 100],
            [18, 43, 50, 56, 65, 67, 69, 79, 96, 96],
            [1, 2, 5, 12, 31, 31, 54, 60, 76, 79],
            [3, 14, 28, 32, 55, 56, 65, 68, 81, 93, 95],
            [2, 7, 22, 24, 27, 30, 33, 40, 46, 69, 70, 72, 78, 84, 94, 97, 97, 97, 100],
            [1, 5, 7, 9, 10, 17, 25, 35, 38, 39, 41, 50, 57, 79, 84, 93, 94],
            [3, 6, 7, 9, 15, 20, 24, 26, 28, 33, 38, 43, 47, 54, 58, 62, 77, 79, 81, 96],
            [6, 6, 19, 21, 37, 38, 42, 44, 59, 62, 70, 80, 91, 96, 100],
            [0, 3, 7, 7, 8, 14, 15, 37, 40, 75, 78, 84, 93],
            [10, 21, 26, 31, 41, 64, 68, 77, 78, 100],
            [4, 15, 17, 27, 28, 30, 32, 35, 35, 36, 37, 44, 48, 76, 88],
        ],
        [
            0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9, 10, 10, 10,
            12, 14, 14, 14, 15, 15, 15, 17, 17, 18, 19, 20, 21, 21, 22, 24, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 28,
            28, 29, 29, 30, 30, 31, 31, 31, 31, 32, 32, 32, 33, 33, 33, 34, 35, 35, 35, 35, 35, 36, 37, 37, 37, 37, 38,
            38, 38, 39, 40, 40, 41, 41, 42, 42, 43, 43, 43, 44, 44, 44, 45, 46, 47, 48, 50, 50, 51, 53, 54, 54, 55, 55,
            55, 56, 56, 56, 57, 58, 58, 58, 59, 60, 62, 62, 64, 65, 65, 67, 68, 68, 69, 69, 69, 69, 70, 70, 72, 72, 73,
            73, 74, 75, 75, 76, 76, 77, 77, 77, 78, 78, 78, 79, 79, 79, 79, 79, 79, 80, 81, 81, 81, 84, 84, 84, 84, 86,
            88, 89, 91, 92, 92, 93, 93, 93, 94, 94, 94, 95, 96, 96, 96, 96, 97, 97, 97, 100, 100, 100, 100, 100, 100,
        ]
    ),
])
class Test:
    def test_solution(self, lists, expected):
        sol = Solution()
        lists = [self._build_list(l) for l in lists]
        head = sol.mergeKLists(lists)
        assert self._format(head) == expected

    def _build_list(self, values: list[int]) -> ListNode | None:
        root = ListNode()
        node = root
        for v in values:
            node.next = node = ListNode(v)

        return root.next

    def _format(self, head: ListNode | None) -> list[int]:
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next

        return values
