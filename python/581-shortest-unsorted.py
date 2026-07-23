class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        s_nums = sorted(nums)
        n = len(nums)
        l, r = 0, n - 1
        if s_nums == nums:
            return 0
        while l < r and nums[l] == s_nums[l]:
            l += 1
        while r > l and nums[r] == s_nums[r]:
            r -= 1
        return r - l + 1


class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        l = r = 0
        max_seen = float("-inf")
        min_seen = float("inf")

        for i in range(n):
            if nums[i] < max_seen:
                r = i
            else:
                max_seen = nums[i]

        if not r:
            return 0

        for i in range(n - 1, -1, -1):
            if nums[i] > min_seen:
                l = i
            else:
                min_seen = nums[i]

        return r - l + 1


# nums = [2, 6, 4, 8, 10, 9, 15]
nums = [1, 2, 3, 4]
# nums = [2, 1]
s = Solution()
print(s.findUnsortedSubarray(nums))
