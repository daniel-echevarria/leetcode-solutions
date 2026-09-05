class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0
        while l < r:
            if height[l] < height[r]:
                max_water = max(height[l] * (r - l), max_water)
                l += 1
            else:
                max_water = max(height[r] * (r - l), max_water)
                r -= 1
        return max_water
