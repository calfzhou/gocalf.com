class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        count_l = count_r = 0
        moves = 0
        for i, c in enumerate(boxes):
            if c == '1':
                count_r += 1
                moves += i

        n = len(boxes)
        answer = [0] * n
        for i, c in enumerate(boxes):
            answer[i] = moves
            if c == '1':
                count_r -= 1
                count_l += 1

            moves += count_l - count_r

        return answer
