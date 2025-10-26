class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        def helper(l, r):
            if l == r:
                return nums[l]
            mid = (l + r) // 2

            left_sum = helper(l, mid)
            right_sum = helper(mid + 1, r)

            cross_left = float("-inf")
            l_sum = 0
            for i in range(mid, l - 1, -1):
                l_sum += nums[i]
                cross_left = max(cross_left, l_sum)

            cross_right = float("-inf")
            r_sum = 0
            for i in range(mid + 1, r + 1):
                r_sum += nums[i]
                cross_right = max(cross_right, r_sum)
            cross_sum = cross_left + cross_right
            res = max(right_sum, left_sum, cross_sum)
            return res

        return helper(0, len(nums) - 1)
