class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        if n == 0:
            return
        if n == 1:
            return nums[0] != val

        l, r = 0, n - 1
        while l < r:
            while l < r and nums[l] != val:
                l += 1
            while l < r and nums[r] == val:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        return l + (nums[l] != val)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        l, r = 0, n - 1

        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        return l


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
s = Solution()
print(s.removeElement(nums, val))
