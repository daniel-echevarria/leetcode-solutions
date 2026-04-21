class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removals = 0
        prev_end = float("-inf")

        for start, end in intervals:
            if start < prev_end:
                removals += 1
                continue
            prev_end = end

        return removals


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
s = Solution()
print(s.eraseOverlapIntervals(intervals))


# Sort intervals by finish time
# then iterate and when they overlap remove the one finishing later
# count removals
