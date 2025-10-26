class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(n, current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum


s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(nums))
