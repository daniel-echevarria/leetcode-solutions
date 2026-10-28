class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        l, r = 0, n - 1
        max_left, max_right = height[l], height[r]
        water = 0

        while l <= r:
            if max_left < max_right:
                max_left = max(max_left, height[l])
                water += max_left - height[l]
                l += 1
            else:
                max_right = max(max_right, height[r])
                water += max_right - height[r]
                r -= 1
        return water
