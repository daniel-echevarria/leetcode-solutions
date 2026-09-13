class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != write:
                    nums[i], nums[write] = nums[write], nums[i]
                write += 1
