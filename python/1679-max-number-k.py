from collections import defaultdict


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0
        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        return count


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        seen = defaultdict(int)
        count = 0
        for n in nums:
            if seen[n] > 0:
                seen[n] -= 1
                count += 1
            else:
                seen[k - n] += 1
        return count


s = Solution()
nums = [3, 1, 3, 4, 3, 3]
k = 6
print(s.maxOperations(nums, 6))
