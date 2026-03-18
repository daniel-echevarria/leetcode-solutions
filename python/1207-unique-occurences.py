from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = Counter(arr)
        occurrences = counts.values()
        return len(occurrences) == len(set(occurrences))


s = Solution()
# arr = [1, 2, 2, 1, 1, 3]
arr = [1, 2]
print(s.uniqueOccurrences(arr))
