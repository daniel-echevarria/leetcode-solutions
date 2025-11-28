class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return [val for pair in zip(nums[:n], nums[n:]) for val in pair]


s = Solution()
nums = [2, 5, 1, 3, 4, 7]
n = 3
print(s.shuffle(nums, n))
