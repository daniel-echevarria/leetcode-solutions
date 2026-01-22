class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l, r = 0, len(arr) - 1

        while l < r:
            mid = (l + r) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l


# nums = [0, 1, 3, 4, 0]
# nums = [18, 29, 38, 59, 98, 100, 99, 98, 90]
nums = [3, 9, 8, 6, 4]


s = Solution()
print(s.peakIndexInMountainArray(nums))
