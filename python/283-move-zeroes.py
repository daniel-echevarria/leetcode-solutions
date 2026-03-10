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


s = Solution()
# nums = [0, 1, 0, 3, 12]
# nums = [1, 0, 1]
nums = [2, 1]
print(s.moveZeroes(nums))

# use two pointers
# iterate so long as r is smaller than the length
# if l and r are both non-zero
# move both by 1
# if l is 0 and r is non-zero
# swap them and move both by 1
# if r is 0 move r by one
