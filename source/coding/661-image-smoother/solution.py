from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        res = [[0] * n for _ in range(m)]

        g = lambda x, y: img[x][y] if 0 <= x < m and 0 <= y < n else None
        neighbors = (
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1),
        )

        for i in range(m):
            for j in range(n):
                s = img[i][j]
                c = 1
                for ud, lr in neighbors:
                    v = g(i+ud, j+lr)
                    if v is not None:
                        s += v
                        c += 1

                res[i][j] = s // c

        return res
