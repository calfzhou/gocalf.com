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
        while True:
            while miss and j < m:
                if (c := s[j]) in needs:
                    needs[c] -= 1
                    if needs[c] == 0:
                        miss -= 1
                j += 1

            if miss:
                break

            while not miss:
                if (c := s[i]) in needs:
                    needs[c] += 1
                    if needs[c] == 1:
                        miss += 1
                i += 1

            if (curr_len := j - i + 1) < min_len or min_len == 0:
                min_len = curr_len
                min_i = i - 1

        return s[min_i:min_i+min_len]
