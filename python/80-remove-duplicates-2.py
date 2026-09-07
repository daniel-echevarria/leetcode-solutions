class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[write - 2]:
                nums[write] = nums[i]
                write += 1
        return write


[0, 0, 1, 1, 1, 1, 2, 3, 3]
