class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, m, r = 0, 0, n - 1

        while m <= r:
            if nums[m] == 2:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
            elif nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                l += 1
                m += 1
            else:
                m += 1


[2, 0, 1]
