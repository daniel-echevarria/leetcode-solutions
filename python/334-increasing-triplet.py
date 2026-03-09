class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        l, r = 0, n - 1
        smallest = nums[l]
        biggest = nums[r]
        while l < r:
            l += 1
            if nums[l] < smallest:
                smallest = nums[l]
            elif smallest < nums[l] < biggest or smallest < nums[r] < biggest:
                return True
            r -= 1
            if nums[r] > biggest:
                biggest = nums[r]
            elif smallest < nums[r] < biggest or smallest < nums[l] < biggest:
                return True
        return smallest < nums[l] < biggest


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        n = len(nums)
        min_suffix = [0] * n
        min_so_far = float("inf")
        for i in range(n):
            min_so_far = min(nums[i], min_so_far)
            min_suffix[i] = min_so_far
        max_so_far = float("-inf")
        for i in range(n - 1, -1, -1):
            max_so_far = max(max_so_far, nums[i])
            if min_suffix[i] < nums[i] < max_so_far:
                return True
        return False


# nums = [5, 4, 3, 2, 1]
# nums = [2, 1, 5, 0, 4, 6]
nums = [1, 5, 0, 4, 1, 3]
s = Solution()
print(s.increasingTriplet(nums))


# use two pointers
# while keeping track of the smallest value from the left
# and the biggest value from the right
# if at any point the next value is between the min and max
# return true
# if l and r are equal return false

# second take:
# build an array of the min so far coming from the left
# then build a max so far coming from the right
# if at any point the current value is between the min so far value for that index
# and the max so far, return true
# after building both arrays return false
