from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        intervals = defaultdict(list)
        for i, char in enumerate(s):
            intervals[char].append(i)
        intervals = sorted(intervals.values())
        res = []
        for inter in intervals:
            if not res:
                res.append(inter)
            if inter[0] <= res[-1][-1]:
                res[-1][-1] = max(inter[-1], res[-1][-1])
            else:
                res.append(inter)
        return [a[-1] - a[0] + 1 for a in res]


# st = "ababcbacadefegdehijhklij"
st = "caedbdedda"
s = Solution()
print(s.partitionLabels(st))

# Algo, iterate and make a map of the intervals
# sort the intervals
# create a result array and iterate through the intervals merging
# the overlapiing ones
# return the lengths of the results
