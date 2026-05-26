from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1

        frequency = [(val, key) for key, val in counts.items()]
        podium = [key for val, key in sorted(frequency, reverse=True)[:k]]
        return podium


nums = [1, 1, 1, 2, 2, 3]
k = 2

s = Solution()
print(s.topKFrequent(nums, k))
