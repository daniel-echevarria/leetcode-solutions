class Solution:
    def trap(self, height: list[int]) -> int:
        L = 0
        R = len(height) - 1
        maxLeft = height[L]
        maxRight = height[R]
        water = 0
        while L < R:
            if maxLeft <= maxRight:
                L += 1
                current = height[L]
                maxLeft = max(maxLeft, current)
                water += maxLeft - current
            elif maxLeft > maxRight:
                R -= 1
                current = height[R]
                maxRight = max(maxRight, current)
                water += maxRight - current
        return water


class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        trapped_water = l = 0

        for i in range(1, n):
            if height[i] < height[l]:
                continue

            trapped_water += min(height[l], height[i]) * (i - l - 1)
            l += 1
            while l < i:
                trapped_water -= height[l]
                l += 1

        r = n - 1
        for j in range(n - 2, l - 1, -1):
            if height[j] < height[r]:
                continue

            trapped_water += min(height[r], height[j]) * (max(r - j - 1, 0))
            r -= 1
            while r > j:
                trapped_water -= height[r]
                r -= 1

        return trapped_water


class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        l, r = 0, n - 1

        max_left = max_right = water = 0

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


s = Solution()
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [4, 2, 0, 3, 2, 5]
# height = [2, 0, 2]
print(s.trap(height))


# Algo
# Declare 5 variables
# L, R, maxLeft, maxRight, water
# Where L, R are indexes starting at 0 and list length - 1
# And maxLeft, maxRight are the respective values in the height list
# And water is the total trapped water
# Launch a loop that runs as long as L is smaller than R
# Then compare the values at L and R
# move the pointer with the smallest value
# when moving the pointer do the following:
# update max(left or right) if needed
# Calculate the trap water and add it to the result
# Return trapped water
