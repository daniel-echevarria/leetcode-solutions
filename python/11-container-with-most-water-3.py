class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        water = 0

        while l < r:
            water = max(water, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return water
