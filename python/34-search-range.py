class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        def helper(l, r):
            while l <= r:
                mid = (l + r) // 2
                if l == r:
                    if nums[l] == target:
                        return l
                    return -1
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    return helper(l, mid)
                else:
                    return helper(mid + 1, r)
            return -1

        index = helper(0, n - 1)
        if index == -1:
            return [-1, -1]
        l = r = index
        while True:
            if l == 0:
                break
            if nums[l - 1] == target:
                l -= 1
                continue
            break
        while True:
            if r == n - 1:
                break
            if nums[r + 1] == target:
                r += 1
                continue
            break

        return [l, r]


s = Solution()
# nums = [5, 7, 7, 8, 8, 10]
# target = 8
nums = [1]
target = 1
print(s.searchRange(nums, target))

# Do a normal binary search then look for the extremities:
