class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        my_set = set(nums)
        count = 1
        while True:
            if count not in my_set:
                return count
            count += 1


# Brute force
# Iterate through nums and make a set of the nums
# then launch a loop that stops when the int is not in the set
