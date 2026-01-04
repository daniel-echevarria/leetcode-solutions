class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i - 1])

        for i, n in enumerate(prefix):
            left_sum = prefix[i - 1] if i > 0 else 0
            right_sum = prefix[-1] - prefix[i]
            if left_sum == right_sum:
                return i
        return -1


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i, n in enumerate(nums):
            if total - left_sum - n == left_sum:
                return i
            left_sum += n
        return -1


s = Solution()
# nums = [1, 7, 3, 6, 5, 6]
# nums = [2, 1, -1]
nums = [3, -3, 5]
print(s.pivotIndex(nums))

# Make a prefix sum array
# Iterate through the prefix array
# if at any point the previous value
# is the same as the last prefix sum minus the current value
# return the index
