class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        if not k:
            return nums

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if not nums:
            return nums

        k %= n
        if not k:
            return nums

        nums[:-k], nums[-k:] = nums[-k:], nums[:-k]
