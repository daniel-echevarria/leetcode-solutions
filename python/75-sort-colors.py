class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, i, r = 0, 0, n - 1
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
        return nums


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        z, t = 0, n - 1

        i = 0
        while i <= t:
            if nums[i] == 0:
                nums[i], nums[z] = nums[z], nums[i]
                i += 1
                z += 1
            elif nums[i] == 2:
                nums[i], nums[t] = nums[t], nums[i]
                t -= 1
            else:
                i += 1
        return nums


nums = [2, 0, 2, 1, 1, 0]
# nums = [2, 0, 1]
# nums = [1, 2, 0]
s = Solution()
print(s.sortColors(nums))
