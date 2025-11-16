class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2, prev1 = 0, 0

        for num in nums:
            curr = max(prev1, prev2 + num)
            prev2, prev1 = prev1, curr
        return curr


s = Solution()
# nums = [1, 2, 3, 1]
# nums = [9, 1, 1, 9]
# nums = [2, 7, 9, 3, 1]
nums = [2, 1, 1, 2]

print(s.rob(nums))
