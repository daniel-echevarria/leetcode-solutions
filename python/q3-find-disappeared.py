class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for n in nums:
            idx = abs(n) - 1
            nums[idx] = -abs(nums[idx])

        return [i + 1 for i, n in enumerate(nums) if n > -1]


s = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(s.findDisappearedNumbers(nums))


# Algo
# make a first path and turn the corresponding index into -1
# make a second path and push the non negative numbers to the result array
