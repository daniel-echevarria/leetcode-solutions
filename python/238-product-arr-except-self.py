class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        num_zeroes = nums.count(0)
        if num_zeroes > 1:
            return [0] * n
        if num_zeroes == 1:
            idx_0 = nums.index(0)
            nums[idx_0] = 1
        total_product = reduce(lambda acc, curr: acc * curr, nums)
        if num_zeroes == 1:
            nums = [0] * n
            nums[idx_0] = total_product
        else:
            for i in range(len(nums)):
                nums[i] = total_product // nums[i]

        return nums


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left_to_right = [1] * n
        right_to_left = [1] * n
        running_left = 1
        running_right = 1
        l, r = 0, len(nums) - 1
        while l < len(nums):
            running_left *= nums[l]
            running_right *= nums[r]
            left_to_right[l] = running_left
            right_to_left[r] = running_right
            l += 1
            r -= 1
        res = []
        for i in range(n):
            if i == 0:
                res.append(right_to_left[1])
                continue
            if i == n - 1:
                res.append(left_to_right[i - 1])
                continue
            res.append(left_to_right[i - 1] * right_to_left[i + 1])
        return res


s = Solution()
nums = [1, 2, 3, 4, 0, 0]
print(s.productExceptSelf(nums))

# compute the total multiplication of the nums
# iterate through nums and replace the value by the previously find total divide by  the current value
