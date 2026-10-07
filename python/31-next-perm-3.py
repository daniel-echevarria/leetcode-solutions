class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        swap = None
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                swap = i
                break

        if swap == None:
            nums.reverse()
            return

        for i in range(n - 1, -1, -1):
            if nums[i] > nums[swap]:
                nums[i], nums[swap] = nums[swap], nums[i]
                break

        nums[swap + 1 :] = nums[swap + 1 :][::-1]
