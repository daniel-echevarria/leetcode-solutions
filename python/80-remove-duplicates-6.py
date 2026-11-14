class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        write = min(2, n)

        for read in range(2, n):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1

        return write
