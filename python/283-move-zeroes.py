class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return nums
        l, r = 0, 1
        while r < n:
            if nums[r] == 0:
                r += 1
                continue
            if nums[l] != 0 and nums[r] != 0:
                if l < r:
                    l += 1
                else:
                    r += 1
                continue
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        i = 0
        while i < n and nums[i] != 0:
            i += 1
        for j in range(i, n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         write = 0
#         for i in range(len(nums)):
#             if nums[i] != 0


s = Solution()
nums = [5, 3, 1, 4, 6, 7, 0, 3, 12]
# nums = [1, 0, 1]
# nums = [2, 1]
print(s.moveZeroes(nums))

# use two pointers
# iterate so long as r is smaller than the length
# if l and r are both non-zero
# move both by 1
# if l is 0 and r is non-zero
# swap them and move both by 1
# if r is 0 move r by one
