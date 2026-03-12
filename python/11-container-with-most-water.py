class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            current_area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, current_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


s = Solution()
h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(s.maxArea(h))


# define two pointers l,r at both ends
# move the smallest one while always computing the total area
# keep updating the total area and when l == r return total area
