class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap_idx = None
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                swap_idx = i
                break

        if swap_idx == None:
            nums[:] = nums[::-1]
            return

        for i in range(n - 1, -1, -1):
            if nums[i] > nums[swap_idx]:
                nums[i], nums[swap_idx] = nums[swap_idx], nums[i]
                break

        nums[swap_idx + 1 :] = nums[swap_idx + 1 :][::-1]


# nums = [1, 3, 2]
nums = [1, 2, 3]
s = Solution()
print(s.nextPermutation(nums))
