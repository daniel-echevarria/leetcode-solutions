class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        n = len(nums)
        nums_sum = sum(nums)

        if nums_sum < p:
            return -1

        remainder = nums_sum % p

        if remainder == 0:
            return 0

        def get_valid_sub_length(i, remainder, count=1):
            if i > n - 1 or nums[i] > remainder:
                return float("inf")
            if nums[i] == remainder:
                return count
            if nums[i] < remainder:
                return get_valid_sub_length(i + 1, remainder - nums[i], count + 1)

        min_length = float("inf")

        for i in range(n - 1):
            min_length = min(min_length, get_valid_sub_length(i, remainder))

        return -1 if min_length == float("inf") else min_length

class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:



# nums = [3, 1, 4, 2]
# p = 6
# nums = [6, 3, 5, 2]
# p = 9
# nums = [1, 2, 3]
# p = 3
# nums = [4, 4, 2]
# p = 7
nums = [17, 3, 16, 12, 3, 19, 1, 8, 5, 8]
p = 54


s = Solution()
print(s.minSubarray(nums, p))
# Algo
# get the sum of nums
# find the remainder after division by p
# find if you can remove a subarray of sum reminder in nums

# To find a subarray of sum reminder do this:
# if the value is bigger than the reminder continue
# if the value is smaller, launch a loop that keeps removing from reminder until left with 0
# if we reach 0 update the min_subarray size
# if we
