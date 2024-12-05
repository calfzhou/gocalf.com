class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i = j = 0
        while i < n and j < n:
            if start[i] == '_':
                i += 1
            elif target[j] == '_':
                j += 1
            elif start[i] != target[j]:
                return False
            elif start[i] == 'L':
                if i < j:
                    return False
                i += 1
                j += 1
            else: # start[i] == 'R'
                if i > j:
                    return False
                i += 1
                j += 1

        return all(start[k] == '_' for k in range(i, n)) and all(target[k] == '_' for k in range(j, n))
