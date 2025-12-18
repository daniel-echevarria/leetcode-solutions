class Solution:
    def isPossible(self, target: list[int]) -> bool:
        n = len(target)
        target.sort()
        print(target)
        found_target = False
        start = [1] * n

        def helper(arr):
            nonlocal found_target
            if arr == target:
                found_target = True
                return
            c_sum = sum(arr)
            if c_sum > target[-1]:
                return False
            for i in range(len(arr)):
                copy = arr.copy()
                copy[i] = c_sum
                helper(copy)

        helper(start)
        return found_target


s = Solution()
target = [9, 3, 5]
print(s.isPossible(target))
# Algo
# Notes:
# If the sum is bigger than then smallest number in the target we ca return false

# First approach:
# We create a heap that will store the possible numbers we can replace
# from the array (set turned heap)
# we iterate on that heap replacing the first char we find
# with the sum recursively.
# if at any point the sum is bigger than the smallest number we return false
# if at some point the array is like the target we change isPossible
