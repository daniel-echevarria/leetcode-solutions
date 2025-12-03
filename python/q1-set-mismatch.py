class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        duplicate = missing = None

        for n in nums:
            idx = abs(n) - 1
            if nums[idx] < 0:
                duplicate = abs(n)
            else:
                nums[idx] *= -1

        for i, n in enumerate(nums):
            if n > 0:
                missing = i + 1
                break

        return [duplicate, missing]


s = Solution()
nums = [1, 1, 5, 3, 2, 7, 6, 4, 8, 9]
print(s.findErrorNums(nums))
