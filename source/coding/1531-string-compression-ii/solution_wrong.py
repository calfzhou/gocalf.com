from collections import defaultdict
from math import inf, log10
from typing import Generator

RLE = tuple[str, int] # (character, run-length)


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if k >= len(s) - 2:
            return len(s) - k

        clen = lambda n: n if n < 2 else int(log10(n)) + 2
        shorten = lambda n: n - 1 if 1 < n < 10 else n - 10**int(log10(n)) + 1
        compressed = list(self.compress(s))

        def best_del():
            best = (-inf, 0, -inf) # gain = dl - dc, dc, -(rle index).
            char_indices = defaultdict(list)
            s_pos = 0 # Position in `s`
            c_pos = 0 # Position in compressed string.

            # Single character deletion, not consider characters merging.
            for idx, (char, cnt) in enumerate(compressed):
                if cnt == 0: continue
                char_indices[char].append((cnt, s_pos, c_pos, idx))
                s_pos += cnt
                c_pos += clen(cnt)
                dl, dc = (2, 2) if k > 1 and cnt == 2 else (1, shorten(cnt))
                if dc <= k:
                    best = max(best, (dl - dc, dc, -idx))

            # Deletions for merging.
            for char, occurs in char_indices.items():
                for i in range(len(occurs) - 1):
                    cnt_i, s_pos_i, c_pos_i, idx_i = occurs[i]
                    for j in range(i + 1, len(occurs)):
                        cnt_j, s_pos_j, c_pos_j, _ = occurs[j]
                        if (dc := s_pos_j - s_pos_i - cnt_i) > k:
                            break
                        cnt = cnt_i + cnt_j
                        dl = c_pos_j - c_pos_i + clen(cnt_j) - clen(cnt)
                        best = max(best, (dl - dc, dc, -(idx_i + 1)))

            return best

        m = len(compressed)
        comp_len = sum(clen(n) for _, n in compressed)
        while k > 0:
            gain, dc, idx = best_del()
            if dc == 0: break
            idx = -idx
            comp_len -= dc + gain
            k -= dc

            # Apply deletion on `compressed`.
            j = idx
            while dc > 0:
                char, cnt = compressed[j]
                if cnt > dc:
                    compressed[j] = (char, cnt - dc)
                else:
                    compressed[j] = (char, 0)
                    j += 1

                dc -= cnt

            if idx > 0 and j < m:
                char_i, cnt_i = compressed[idx-1]
                char_j, cnt_j = compressed[j]
                if char_j == char_i: # Merging happens.
                    compressed[idx-1] = (char_i, cnt_i + cnt_j)
                    compressed[j] = (char_j, 0)

        return comp_len

    def compress(self, s: str) -> Generator[RLE, None, None]:
        n = len(s)
        prev = s[0]
        cnt = 1
        for i in range(1, n + 1):
            if i < n and (c := s[i]) == prev:
                cnt += 1
                continue

            yield prev, cnt

            if i < n:
                prev = c
                cnt = 1
