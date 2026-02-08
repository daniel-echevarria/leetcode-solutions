import bisect


class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        start_and_idx = []
        for i, interval in enumerate(intervals):
            start_and_idx.append([interval[0], i])
        start_and_idx.sort()
        print(start_and_idx)
        res = []
        for x in intervals:
            idx = bisect.bisect_left(start_and_idx, [x[1]])
            if idx == len(start_and_idx):
                res.append(-1)
            else:
                res.append(start_and_idx[idx][1])
        return res


s = Solution()
intervals = [[3, 4], [2, 3], [1, 2]]
print(s.findRightInterval(intervals))

# Algo, create an array with the starts and the indexes, then sort that array
# then iterate map through the intervals and for each end  bisect  where they should be inserted in the start list
# return the idx of the following start
# if the idx is the size of start_and_idx
