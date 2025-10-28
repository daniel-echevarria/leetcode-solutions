class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        if not nums:
            return None
        if n == 1:
            return 0

        peak_found = None

        def peak_finder(l, r):
            nonlocal peak_found
            if peak_found:
                return
            if l == r:
                if l == 0:
                    if nums[l] > nums[l + 1]:
                        peak_found = l
                elif l == n - 1:
                    if nums[l] > nums[l - 1]:
                        peak_found = l
                elif nums[l - 1] < nums[l] < nums[l + 1]:
                    peak_found = l
                return
            mid = (l + r) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                peak_found = mid
                return mid
            if nums[mid - 1] > nums[mid + 1]:
                peak_finder(l, mid)
            else:
                peak_finder(mid + 1, r)

        peak_finder(0, n - 1)

        return peak_found


# Algo:
# find the middle
# if the middle is a peak return early
# otherwise search both sides for peak

s = Solution()
# nums = [1, 2, 3, 1]
# nums = [1, 2, 1, 3, 5, 6, 4]
nums = [1]
print(s.findPeakElement(nums))
