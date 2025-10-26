class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        current_sum_left = current_sum_right = max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum_left = max(nums[i], current_sum_left + nums[i])
            max_sum = max(max_sum, current_sum_left)

        for j in range(-1, -len(nums), -1):
            current_sum_right = max(nums[j], current_sum_right + nums[j])
            max_sum = max(max_sum, current_sum_right)

        return max_sum


s = Solution()
nums = [-2, 4, -5, 4, -5, 9, 4]
print(s.maxSubarraySumCircular(nums))
