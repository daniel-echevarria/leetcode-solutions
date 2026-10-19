class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        write = 1

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[write] = nums[i]
                write += 1
        return write
