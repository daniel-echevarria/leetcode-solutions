class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        min_diff = float("inf")
        curr_min_diff = float("inf")
        curr_sum = float("inf")
        for i, v in enumerate(nums):
            j, k = 0, len(nums) - 1
            while j < k:
                if j == i:
                    j += 1
                if k == i:
                    k -= 1
                if j == k:
                    return closest
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == target:
                    return target
                if curr_sum < target:
                    j += 1
                else:
                    k -= 1
                diff = abs(curr_sum - target)
                if diff > curr_min_diff:
                    if curr_min_diff < min_diff:
                        min_diff = curr_min_diff
                        closest = curr_sum
                    break
                curr_min_diff = diff
            if curr_min_diff < min_diff:
                min_diff = curr_min_diff
                closest = curr_sum
            curr_min_diff = float("inf")
        return closest


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        curr_sum = nums[0] + nums[1] + nums[2]
        closest = curr_sum

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]

                if abs(target - curr_sum) < abs(target - closest):
                    closest = curr_sum

                if curr_sum < target:
                    j += 1
                elif curr_sum > target:
                    k -= 1
                else:
                    return target
        return closest


# Algo
# sort the array
# for each value at index i
# get as close as possible ( the moment you get farther continue)
# keep track of the closest overall
# return closes overall
# if exact match return target

# nums = [-1, 2, 1, -4]
# target = 1
# nums = [0, 1, 2]
# target = 0
nums = [0, 0, 0]
target = 1
s = Solution()
print(s.threeSumClosest(nums, target))
