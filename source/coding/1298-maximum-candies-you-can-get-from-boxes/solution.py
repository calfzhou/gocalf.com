class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        boxes = [False] * len(status) # `boxes[i] = True` means I have box i but cannot open it.
        stack: list[int] = [] # Boxes to be processed.
        for i in initialBoxes:
            if status[i]:
                stack.append(i)
            else:
                boxes[i] = True

        total = 0
        while stack:
            i = stack.pop()
            total += candies[i]
            for j in keys[i]:
                if boxes[j]:
                    boxes[j] = False
                    stack.append(j)
                else:
                    status[j] = 1

            for j in containedBoxes[i]:
                if status[j]:
                    stack.append(j)
                else:
                    boxes[j] = True

        return total
