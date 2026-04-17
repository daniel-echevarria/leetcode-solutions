class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        start = 0
        for n in nums:
            start ^= n
        return start


class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        res = 0
        for n in nums:
            res ^= n
        return res


s = Solution()
nums = [2, 2, 1]
print(s.singleNumber(nums))
