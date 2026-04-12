class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2, prev1 = 0, 0

        for num in nums:
            curr = max(prev1, prev2 + num)
            prev2, prev1 = prev1, curr
        return curr


class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        if n < 4:
            return max(nums[1], nums[0] + nums[2])
        maxMoney = [0] * n
        maxMoney[0] = nums[0]
        maxMoney[1] = nums[1]
        maxMoney[2] = nums[2] + nums[0]
        for i in range(3, n):
            maxMoney[i] = max(maxMoney[i - 2], maxMoney[i - 3]) + nums[i]
        return max(maxMoney)


s = Solution()
# nums = [1, 2, 3, 1]
# nums = [9, 1, 1, 9]
# nums = [2, 7, 9, 3, 1]
# nums = [2, 1, 1, 2]
nums = [1, 7, 9, 2]


print(s.rob(nums))
