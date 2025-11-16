class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        money = {}
        money[0] = nums[0]
        money[1] = nums[1]
        money[2] = nums[2] + nums[0]
        max_money = max(money[0], money[1], money[2])
        for i in range(3, n):
            money[i] = nums[i] + max(money[i - 2], money[i - 3])
            max_money = max(money[i], max_money)
        return max_money


s = Solution()
# nums = [1, 2, 3, 1]
# nums = [9, 1, 1, 9]
nums = [2, 7, 9, 3, 1]

print(s.rob(nums))
