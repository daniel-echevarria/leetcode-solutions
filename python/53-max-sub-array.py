class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        def helper(l, r):
            if l == r:
                return nums[l]
            mid = (l + r) // 2

            left_sum = helper(l, mid)
            right_sum = helper(mid + 1, r)

            cross_left = float("-inf")
            ls = 0
            for i in range(mid, l - 1, -1):
                ls += nums[i]
                cross_left = max(cross_left, ls)

            cross_right = float("-inf")
            rs = 0
            for i in range(mid + 1, r + 1):
                rs += nums[i]
                cross_right = max(cross_right, rs)

            sum_cross = cross_left + cross_right
            res = max(left_sum, right_sum, sum_cross)

            return res

        return helper(0, len(nums) - 1)
