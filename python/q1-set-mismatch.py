from collections import defaultdict


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        miss_dup = [None] * 2

        for i in range(1, len(nums) + 1):
            if i not in count:
                miss_dup[1] = i
            elif count[i] == 2:
                miss_dup[0] = i
        return miss_dup


s = Solution()
nums = [1, 3, 3, 4]
print(s.findErrorNums(nums))
