class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # Left side is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # right side is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


s = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
# nums = [5, 1, 3]
print(s.search(nums, 1))
# Algo
# Get the middle of the array
# get the first value of the array
# if the value is between the first and mid
# recurse there otherwise recurse on the other side
