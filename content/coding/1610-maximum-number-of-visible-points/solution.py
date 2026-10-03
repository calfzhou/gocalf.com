from math import atan2, pi, radians


class Solution:
    def visiblePoints(self, points: list[list[int]], angle: int, location: list[int]) -> int:
        overlap = 0
        thetas = []
        for x, y in points:
            if x == location[0] and y == location[1]:
                overlap += 1
            else:
                thetas.append(atan2(y - location[1], x - location[0]) - pi) # (-2pi, 0]

        if not thetas: return overlap

        pi2 = 2 * pi
        fov = radians(angle)
        thetas.sort()
        n = len(thetas)
        l = -n
        theta_l = thetas[l]
        for r in range(1 - n, n):
            theta_r = thetas[r] if r < 0 else thetas[r] + pi2
            if theta_r > fov: break
            if theta_r - theta_l > fov:
                l += 1
                theta_l = thetas[l] if l < 0 else thetas[l] + pi2
        else:
            r = n

        return overlap + r - l
