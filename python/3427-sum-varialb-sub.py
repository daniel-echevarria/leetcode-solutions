class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            start = max(0, i - nums[i])
            total += sum(nums[start : i + 1])
        return total


s = Solution()
nums = [2, 3, 1]
print(s.subarraySum(nums))
