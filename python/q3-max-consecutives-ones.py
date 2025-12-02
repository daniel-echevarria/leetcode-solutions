class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_consecutive = current = 0

        for n in nums:
            if n == 0:
                max_consecutive = max(max_consecutive, current)
                current = 0
            else:
                current += 1

        return max(max_consecutive, current)


s = Solution()
nums = [1, 1, 0, 1, 1, 1]
print(s.findMaxConsecutiveOnes(nums))
