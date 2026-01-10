class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0

        for i, n in enumerate(nums):
            if right_sum - left_sum - n == 0:
                return i
            left_sum += n
            right_sum -= n
        return -1


s = Solution()
nums = [2, 3, -1, 8, 4]
print(s.findMiddleIndex(nums))


# Algo:
# get the total sum
# enumerate through nums
# while keeping track of the left sum
# if any point the total sum minus the left sum minus
# the current value equals the left sum
# return the index
# after iteration return -1
