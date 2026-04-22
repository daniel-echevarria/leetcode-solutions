class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows = 1
        prev_end = points[0][1]

        for start, end in points[1:]:
            if start <= prev_end:
                continue
            arrows += 1
            prev_end = end
        return arrows


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
s = Solution()
print(s.findMinArrowShots(points))
