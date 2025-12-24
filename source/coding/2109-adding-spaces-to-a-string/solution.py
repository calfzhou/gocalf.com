class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        def ranges():
            prev = 0
            for val in spaces:
                yield prev, val
                prev = val

            yield spaces[-1], len(s)

        return ' '.join(s[b:e] for b, e in ranges())
