class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(reverse=True)
        res = []
        while intervals:
            start, end = intervals.pop()
            if intervals and end >= intervals[-1][0]:
                _, n_end = intervals.pop()
                final_end = max(end, n_end)
                intervals.append([start, final_end])
                continue
            res.append([start, end])
        return res


s = Solution()
nums = [[4, 7], [1, 4]]
print(s.merge(nums))
