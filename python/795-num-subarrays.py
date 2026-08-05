class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        def count(maxVal):
            curr = 0
            res = 0

            for val in nums:
                if val > maxVal:
                    curr = 0
                else:
                    curr += 1
                res += curr

            return res

        return count(right) - count(left - 1)


nums = [2, 9, 2, 5, 6]
left = 2
right = 8

s = Solution()
print(s.numSubarrayBoundedMax(nums, left, right))
