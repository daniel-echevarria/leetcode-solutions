class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        def search_left():
            l, r = 0, n - 1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target and (mid == 0 or nums[mid] > nums[mid - 1]):
                    return mid
                elif nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1

        def search_right():
            l, r = 0, n - 1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target and (mid == n - 1 or nums[mid] < nums[mid + 1]):
                    return mid
                elif nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1

        left = search_left()
        right = search_right()
        if left == None or right == None:
            return [-1, -1]
        return [left, right]


s = Solution()
# nums = [5, 7, 7, 8, 8, 10]
# target = 8
# nums = [1]
# target = 1
nums = [1, 2, 3]
target = 1

print(s.searchRange(nums, target))

# Do a normal binary search then look for the extremities:
