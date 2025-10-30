class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        def get_median(nums):
            if not nums:
                return 0
            n = len(nums)
            if n < 2:
                return nums[0]
            l, r = 0, n - 1
            mid = (l + r) // 2
            if n % 2 == 0:
                return (nums[mid] + nums[mid + 1]) / 2
            else:
                return nums[mid]

        median1 = get_median(nums1)
        median2 = get_median(nums2)
        if not median1:
            return median2
        elif not median2:
            return median2
        return (median1 + median2) / 2


s = Solution()
nums1 = [2]
nums2 = []
print(s.findMedianSortedArrays(nums1, nums2))
