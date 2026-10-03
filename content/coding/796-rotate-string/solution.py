class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal):
            return False

        for r in range(n):
            for i in range(n):
                if goal[i] != s[i-r]:
                    break
            else:
                return True

        return False
