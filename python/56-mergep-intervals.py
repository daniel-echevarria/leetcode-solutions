# class Solution:
#     def merge(self, intervals: list[list[int]]) -> list[list[int]]:
#         intervals.sort(reverse=True)
#         res = []
#         while intervals:
#             start, end = intervals.pop()
#             if intervals and end >= intervals[-1][0]:
#                 _, n_end = intervals.pop()
#                 final_end = max(end, n_end)
#                 intervals.append([start, final_end])
#                 continue
#             res.append([start, end])
#         return res


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
s = Solution()
print(s.merge(intervals))
