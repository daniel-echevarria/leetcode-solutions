class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = current_sum = nums[0]

        for n in nums[1:]:
            current_sum = max(n, current_sum + n)
            max_sum = max(current_sum, max_sum)
        return max_sum
