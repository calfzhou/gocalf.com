class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 1 == 1:
            return False

        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
                continue

            if not stack:
                return False
            left = stack.pop()
            if left == '(' and c != ')' or left == '{' and c != '}' or left == '[' and c != ']':
                return False

        return len(stack) == 0
