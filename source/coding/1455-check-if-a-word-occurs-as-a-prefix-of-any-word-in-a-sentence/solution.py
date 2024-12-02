class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        m = len(searchWord)
        idx = 1
        j = 0
        for c in sentence:
            if c == ' ':
                idx += 1
                j = 0
            elif j < m and searchWord[j] == c:
                j += 1
                if j == m:
                    return idx
            else:
                j = m # The idx-th word is not possible.

        return -1
