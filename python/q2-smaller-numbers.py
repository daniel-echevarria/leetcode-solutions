class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        prev = -1
        count_smaller = {}
        for i, n in enumerate(sorted_nums):
            if n == prev:
                continue
            prev = n
            count_smaller[n] = i

        return [count_smaller[x] for x in nums]


s = Solution()
nums = [8, 1, 2, 2, 3]
print(s.smallerNumbersThanCurrent(nums))


# Algo make a set from the array (to get unique values)
# Then transform it back to an array
# then create a map that for each value maps to the number of values before
# (current index)
# map the original array to the values in map
