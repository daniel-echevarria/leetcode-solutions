class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        def peak_finder(l, r):
            if l == r:
                return r
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return peak_finder(l, mid)
            else:
                return peak_finder(mid + 1, r)

        return peak_finder(0, len(nums) - 1)
