from collections import defaultdict


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = defaultdict(list)

        for i, n in enumerate(nums):
            indices[n].append(i)

        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            current_sum = nums[l] + nums[r]
            if current_sum == target:
                return [indices[nums[l]].pop(), indices[nums[r]].pop()]
            if current_sum < target:
                l += 1
            if current_sum > target:
                r -= 1


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        possible_pairs = {}

        for i, n in enumerate(nums):
            if n in possible_pairs:
                return [possible_pairs[n], i]
            possible_pairs[target - n] = i


s = Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums, target))

# Algo
# Sort the array
# use two pointers l and r
# launch a loop that runs until the sum of the values at l and r
# equal the target or that l == r
# return l an r
