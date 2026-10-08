class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        water = 0
        max_left = height[0]
        max_right = height[n - 1]
        l, r = 1, n - 2

        while l <= r:
            if max_left <= max_right:
                max_left = max(max_left, height[l])
                water += max_left - height[l]
                l += 1
            else:
                max_right = max(max_right, height[r])
                water += max_right - height[r]
                r -= 1
        return water
