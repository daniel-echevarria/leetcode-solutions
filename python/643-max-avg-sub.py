class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        l, r = 0, k
        while r < len(nums):
            current_sum -= nums[l]
            current_sum += nums[r]
            l += 1
            r += 1
            max_sum = max(current_sum, max_sum)
        return max_sum / k


s = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(s.findMaxAverage(nums, k))
