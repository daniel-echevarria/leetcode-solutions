class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if not n:
            return

        k %= n
        if not k:
            return

        portion = nums[-k:]
        nums[-k:] = []
        nums[:0] = portion
        return nums


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        nums.reverse()
        nums[k:] = reversed(nums[k:])
        nums[:k] = reversed(nums[:k])

        return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
s = Solution()
print(s.rotate(nums, k))
