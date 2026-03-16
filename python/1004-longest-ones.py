class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = r = 0
        tokens = k
        max_len = 0
        while r < len(nums):
            if nums[r] == 1:
                r += 1
            elif nums[r] == 0:
                if tokens:
                    tokens -= 1
                    r += 1
                else:
                    if nums[l] == 0:
                        tokens += 1
                    l += 1
            max_len = max(r - l, max_len)
        return max_len


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1

            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1


s = Solution()
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
# nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# k = 3
print(s.longestOnes(nums, k))


# Keep a counter of how many tokens used from k as moving through the list
# as long as the value is 1 just keep going, if it's 0 use a token
# if there are no tokens left, move the left until there are tokens again
# do that until the end of the array
