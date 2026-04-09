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


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if mid == 0:
                return 0 if nums[0] > nums[1] else 1

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            elif nums[mid] < nums[mid - 1]:
                r = mid - 1
            else:
                return mid
        return l


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return l


nums = [1, 2, 1, 3, 5, 6, 4]
s = Solution()
print(s.findPeakElement(nums))
