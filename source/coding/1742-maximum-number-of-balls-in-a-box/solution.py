from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def sum_digits(num: int) -> int:
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s

        boxes: dict[int, int] = defaultdict(int) # box number -> number of balls
        box_num = sum_digits(lowLimit - 1)
        for num in range(lowLimit, highLimit + 1):
            if num % 10 == 0:
                box_num = sum_digits(num)
            else:
                box_num += 1

            boxes[box_num] += 1

        return max(boxes.values())
