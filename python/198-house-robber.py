class Solution:
    def rob(self, nums: list[int]) -> int:
        even_sum = 0
        odd_sum = 0
        for i in range(len(nums)):
            money = nums[i]
            if i % 2 == 0:
                even_sum += money
            else:
                odd_sum += money
        return max(even_sum, odd_sum)


s = Solution()
nums = [1, 2, 3, 1]
print(s.rob(nums))
# Algo sum the values at even intervals
# sum the values at odd intervals
# return the biggest sum
