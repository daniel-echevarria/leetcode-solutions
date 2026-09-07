class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        water = 0
        l, r = 0, n - 1
        max_left = max_right = 0

        while l <= r:
            if max_left < max_right:
                max_left = max(height[l], max_left)
                water += max_left - height[l]
                l += 1
            else:
                max_right = max(height[r], max_right)
                water += max_right - height[r]
                r -= 1
        return water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
