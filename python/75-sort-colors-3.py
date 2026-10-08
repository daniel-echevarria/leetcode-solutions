class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a, b, c = 0, 0, n - 1

        while b <= c:
            if nums[b] == 0:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b += 1
            elif nums[b] == 1:
                b += 1
            else:
                nums[b], nums[c] = nums[c], nums[b]
                c -= 1
