class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        return l


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write] = nums[i]
                write += 1
        return write
