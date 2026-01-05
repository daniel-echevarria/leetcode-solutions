class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = []
        total = 0

        for n in nums:
            total += n
            res.append(total)

        return res


s = Solution()
nums = [1, 2, 3, 4]
print(s.runningSum(nums))

# Algo
# Define an array results with just the first element of nums
# iterate through nums from index 1 and append to res
# the sum of the current value + the previous value of res
# return res
