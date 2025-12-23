class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        if m < len(t):
            return ''

        needs: dict[str, int] = {} # character: number of this character needed.
        for c in t:
            needs[c] = needs.get(c, 0) + 1
        miss = len(needs)

        min_i = min_len = 0
        i = j = 0
        while not (miss and j == m):
            if miss:
                if (c := s[j]) in needs:
                    needs[c] -= 1
                    if needs[c] == 0:
                        miss -= 1
                j += 1
            else:
                if (c := s[i]) in needs:
                    needs[c] += 1
                    if needs[c] == 1:
                        miss += 1
                        if (curr_len := j - i) < min_len or min_len == 0:
                            min_i = i
                            min_len = curr_len
                i += 1

        return s[min_i:min_i+min_len]
