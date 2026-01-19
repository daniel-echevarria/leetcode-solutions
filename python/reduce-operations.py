class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort()
        operations = distance = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                distance += 1
            operations += distance
        return operations


# Algo
# make a sorted and unique array out of nums
# iterate from the second index
# add to the total the index times the count of that el in nums
# return the total
s = Solution()
# nums = [5, 1, 3]
nums = [1, 1, 2, 2, 3]
print(s.reductionOperations(nums))
