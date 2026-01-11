class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        prefix = []
        curr = 0
        for n in nums:
            curr += n
            prefix.append(curr)
        curr = 0
        answer = []
        for i in range(len(nums) - 1, -1, -1):
            curr += nums[i]
            answer.append(abs(prefix[i] - curr))
        answer.reverse()
        return answer


s = Solution()
nums = [10, 4, 8, 3]
print(s.leftRightDifference(nums))


# Algo
# create both prefix sums
# return the difference
