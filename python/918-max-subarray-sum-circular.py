class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        current_sum_left = current_sum_right = max_sum = float("-inf")
        mid = len(nums) // 2

        for i in range(0, len(nums)):
            current_sum_left = max(nums[i], current_sum_left + nums[i])
            max_sum = max(max_sum, current_sum_left)

        for j in range(mid - 1, -len(nums) + 1, -1):
            current_sum_right = max(nums[j], current_sum_right + nums[j])
            max_sum = max(max_sum, current_sum_right)

        return max_sum


s = Solution()
# nums = [-2, 4, -5, 4, -5, 9, 4]
# nums = [3, -1, 2, -1]
# nums = [9, 8, 4, -7]
nums = [5, 6, 1, 4, 8, -8, 7, -5, 3]
print(s.maxSubarraySumCircular(nums))
