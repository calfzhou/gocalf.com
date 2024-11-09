from typing import List

R = 1
L = R << 1
B = L << 1
T = B << 1

TB = T | B
LR = L | R
LB = L | B
RT = R | T


class Cluster:
    def __init__(self, circle: List[int], edges: int):
        self.circles = [circle]
        self.edges = edges # cross edges bit map 0bTBLR

        x, y, r = circle
        self.top = y + r
        self.bottom = y - r
        self.left = x - r
        self.right = x + r

    def merge(self, other: 'Cluster'):
        self.circles.extend(other.circles)
        self.edges |= other.edges

        self.top = max(self.top, other.top)
        self.bottom = min(self.bottom, other.bottom)
        self.left = min(self.left, other.left)
        self.right = max(self.right, other.right)

    def is_out_of_bound(self, circle: List[int]):
        x, y, r = circle
        return x + r < self.left or x - r > self.right or y + r < self.bottom or y - r > self.top


class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        clusters = []
        for circle in circles:
            edges, out_of_rect = self._calc_crossed_edges(xCorner, yCorner, circle)
            if self._is_unreachable(edges):
                return False

            if out_of_rect:
                continue

            new_clusters = []
            this_cluster = Cluster(circle, edges)
            for cluster in clusters:
                # A quick prune.
                if cluster.is_out_of_bound(circle):
                    new_clusters.append(cluster)
                    continue

                for circle2 in cluster.circles:
                    if self._are_circles_connected_inside_rect(circle, circle2, xCorner, yCorner):
                        this_cluster.merge(cluster)
                        if self._is_unreachable(this_cluster.edges):
                            return False
                        break
                else:
                    new_clusters.append(cluster)

            new_clusters.append(this_cluster)
            clusters = new_clusters

        return True

    def _are_circles_connected(self, circle1: List[int], circle2: List[int]) -> bool:
        x1, y1, r1 = circle1
        x2, y2, r2 = circle2

        # Prune by bound box.
        if x2 + r2 < x1 - r1 or x2 - r2 > x1 + r1 or y2 + r2 < y1 - r1 or y2 - r2 > y1 + r1:
            return False

        distance_square = (x1 - x2) ** 2 + (y1 - y2) ** 2
        radius_sum_square = (r1 + r2) ** 2
        return distance_square <= radius_sum_square

    def _are_circles_connected_inside_rect(self, circle1, circle2, xCorner, yCorner) -> bool:
        if not self._are_circles_connected(circle1, circle2):
            return False

        x1, y1, r1 = circle1
        x2, y2, r2 = circle2

        # (x1, y1)--(x, y) : (x, y)--(x2, y2) = r1 : r2
        # Check if (x, y) inside rect.
        if (-x1 * (r1 + r2) <= (x2 - x1) * r1 <= (xCorner - x1) * (r1 + r2) and
            -y1 * (r1 + r2) <= (y2 - y1) * r1 <= (yCorner - y1) * (r1 + r2)):
            return True

        return False

    def _is_h_line_cross_circle(self, left: int, right: int, y: int, circle: List[int]) -> bool:
        cx, cy, r = circle

        # Check if line is far away from circle.
        if abs(y - cy) > r:
            return False

        # Check if left endpoint inside circle.
        r_square = r ** 2
        if (left - cx) ** 2 + (y - cy) ** 2 <= r_square:
            return True

        # Check if right endpoint inside circle.
        if (right - cx) ** 2 + (y - cy) ** 2 <= r_square:
            return True

        # Check if the two endpoints apart from the perpendicular line.
        if left < cx < right:
            return True

        return False

    def _is_v_line_cross_circle(self, bottom: int, top: int, x: int, circle: List[int]) -> bool:
        cx, cy, r = circle

        # Check if line is far away from circle.
        r_square = r ** 2
        if abs(x - cx) > r:
            return False

        # Check if bottom endpoint inside circle.
        if (x - cx) ** 2 + (bottom - cy) ** 2 <= r_square:
            return True

        # Check if top endpoint inside circle.
        if (x - cx) ** 2 + (top - cy) ** 2 <= r_square:
            return True

        # Check if the two endpoints apart from the perpendicular line.
        if bottom < cy < top:
            return True

        return False

    def _calc_crossed_edges(self, xCorner, yCorner, circle) -> tuple[int, bool]:
        edges = 0

        if self._is_h_line_cross_circle(0, xCorner, yCorner, circle):
            edges |= T

        if self._is_h_line_cross_circle(0, xCorner, 0, circle):
            edges |= B

        if self._is_v_line_cross_circle(0, yCorner, xCorner, circle):
            edges |= R

        if self._is_v_line_cross_circle(0, yCorner, 0, circle):
            edges |= L

        cx, cy, _ = circle
        out_of_rect = edges == 0 and not (0 < cx < xCorner and 0 < cy < yCorner)

        return edges, out_of_rect

    def _is_unreachable(self, edges: int) -> bool:
        return edges & TB == TB or edges & LR == LR or edges & LB == LB or edges & RT == RT
