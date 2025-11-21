class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        memo = [1] * (n + 1)

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[i], memo[j] + 1)

        return max(memo)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
s = Solution()
print(s.lengthOfLIS(nums))
