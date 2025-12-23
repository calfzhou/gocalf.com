class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        write = 0
        prev = ''
        cnt = 0
        for i in range(n + 1):
            if i < n and (c := chars[i]) == prev:
                cnt += 1
                continue

            if cnt > 1:
                for d in str(cnt):
                    chars[write] = d
                    write += 1

            if i < n:
                chars[write] = prev = c
                write += 1
                cnt = 1

        del chars[write:]
        return len(chars)
