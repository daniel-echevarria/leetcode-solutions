class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        l, r = 1, n - 2
        max_left, max_right = height[0], height[n - 1]
        water = 0

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


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution()
print(s.trap(height))
