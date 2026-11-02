class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        write = 0
        for num in nums:
            if num != 0:
                nums[write] = num
                write += 1

        for i in range(write, n):
            nums[i] = 0


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        write = 0

        for read in range(n):
            if nums[read] != 0:
                if read != write:
                    nums[read], nums[write] = nums[write], nums[read]
                write += 1
