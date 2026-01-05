class Solution:
    def minStartValue(self, nums: list[int]) -> int:

        deepest = 0
        current = 0

        for n in nums:
            current += n
            deepest = min(deepest, current)

        return 1 - deepest


s = Solution()
# nums = [-3, 2, -3, 4, 2]
# nums = [1, 2]
nums = [1, -2, -3]
print(s.minStartValue(nums))

# Algo:
# Iterate through the nums while keeping track of the current total
# Track the min current total overall
# return the absolute value of min + 1 if the min current is below 1
# otherwise return 1
