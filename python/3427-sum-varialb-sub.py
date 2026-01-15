from itertools import accumulate


class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        acc = list(accumulate(nums))
        for i in range(n):
            start = max(0, i - nums[i]) - 1
            total += acc[i]
            if start >= 0:
                total -= acc[start]
        return total


s = Solution()
nums = [2, 3, 1]
print(s.subarraySum(nums))
