class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        operations = 0
        ordered_nums = sorted(nums, reverse=True)
        unique_sorted = sorted(list(set(nums)))
        for i, n in enumerate(unique_sorted):
            count = 0
            while ordered_nums and ordered_nums[-1] == n:
                ordered_nums.pop()
                count += 1
            operations += count * i
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
