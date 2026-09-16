class Solution:
    def mostCompetitive(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        stack = [nums[0]]
        for i in range(1, n):
            while (
                stack and nums[i] < stack[-1] and (len(stack) + len(nums) - i - 1) >= k
            ):
                stack.pop()
            stack.append(nums[i])
        return stack[:k]


# nums = [2, 4, 3, 3, 5, 4, 9, 6]
# k = 4
nums = [71, 18, 52, 29, 55, 73, 24, 42, 66, 8, 80, 2]
k = 3
s = Solution()
print(s.mostCompetitive(nums, k))
