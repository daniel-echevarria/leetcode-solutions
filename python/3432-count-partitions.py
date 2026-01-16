class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        total = sum(nums)
        if total % 2 == 0:
            return len(nums) - 1
        return 0
        count = left = 0
        for n in nums:
            left += n
            if left == total:
                return count
            right = total - left
            difference = left - right
            if difference % 2 == 0:
                count += 1


s = Solution()
# nums = [10, 10, 3, 7, 6]
# nums = [1, 2, 2]
nums = [2, 4, 6, 8]

print(s.countPartitions(nums))
