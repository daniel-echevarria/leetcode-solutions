class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        min_sum = current_min = float("inf")
        max_sum = current_max = float("-inf")
        total_sum = 0

        for num in nums:
            current_min = min(current_min + num, num)
            min_sum = min(min_sum, current_min)
            current_max = max(current_max + num, num)
            max_sum = max(max_sum, current_max)
            total_sum += num
        if max_sum < 0:
            return max_sum
        return max(max_sum, (total_sum - min_sum))


s = Solution()
# nums = [-2, 4, -5, 4, -5, 9, 4]
# nums = [3, -1, 2, -1]
# nums = [9, 8, 4, -7]
# nums = [5, 6, 1, 4, 8, -8, 7, -5, 3]
nums = [1, -2, 3, -2]
print(s.maxSubarraySumCircular(nums))
