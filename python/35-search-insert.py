class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        def helper(l, r):
            if l == r:
                if nums[l] < target:
                    return l + 1
                if nums[l] > target:
                    return l
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return helper(mid + 1, r)
            else:
                return helper(l, mid)

        return helper(0, len(nums) - 1)


s = Solution()
nums = [1, 3, 5, 6, 7]
print(s.searchInsert(nums, 7))
