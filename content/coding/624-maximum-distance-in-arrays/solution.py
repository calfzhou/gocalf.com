max2 = lambda a, b: a if a >= b else b

class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        if arrays[0][-1] >= arrays[1][-1]:
            mxi, mx, mx2 = 0, arrays[0][-1], arrays[1][-1]
        else:
            mxi, mx, mx2 = 1, arrays[1][-1], arrays[0][-1]

        if arrays[0][0] <= arrays[1][0]:
            mni, mn, mn2 = 0, arrays[0][0], arrays[1][0]
        else:
            mni, mn, mn2 = 1, arrays[1][0], arrays[0][0]

        for i in range(2, len(arrays)):
            if arrays[i][-1] >= mx:
                mxi, mx, mx2 = i, arrays[i][-1], mx
            elif arrays[i][-1] >= mx2:
                mx2 = arrays[i][-1]

            if arrays[i][0] <= mn:
                mni, mn, mn2 = i, arrays[i][0], mn
            elif arrays[i][0] <= mn2:
                mn2 = arrays[i][0]

        if mxi != mni:
            return mx - mn
        else:
            return max2(mx - mn2, mx2 - mn)
