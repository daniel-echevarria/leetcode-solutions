from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        seen_running_total = defaultdict(int)

        running_total = 0
        seen_running_total[0] = 1
        res = 0
        for i, char in enumerate(nums):
            running_total += char
            res += seen_running_total[running_total - k]
            seen_running_total[running_total] += 1
        return res


nums = [1, 2, 3, 7, -4]
k = 3
# nums = [1]
# k = 0
s = Solution()
print(s.subarraySum(nums, k))
