class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float("inf")
        res = 0

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                diff = abs(target - curr_sum)
                if diff < closest:
                    res = curr_sum
                    closest = diff
                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    return curr_sum
        return res


nums = [-1, 2, 1, -4]
target = 1

s = Solution()
print(s.threeSumClosest(nums, target))
