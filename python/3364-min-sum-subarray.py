class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float("inf")
        curr = 0
        for i in range(l, r + 1):
            for j in range(0, n - i + 1):
                curr = sum(nums[j : j + i])
                if curr > 0:
                    min_sum = min(curr, min_sum)
        return -1 if min_sum == float("inf") else min_sum


s = Solution()
# nums = [3, -2, 1, 4]
nums = [7, 3]
print(s.minimumSumSubarray(nums, 2, 2))
