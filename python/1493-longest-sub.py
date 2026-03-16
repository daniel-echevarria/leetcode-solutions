class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        l = 0
        token = 1
        for r in range(len(nums)):
            if nums[r] == 0:
                token -= 1

            if token < 0:
                if nums[l] == 0:
                    token += 1
                l += 1
        return r - l


s = Solution()
nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
print(s.longestSubarray(nums))
