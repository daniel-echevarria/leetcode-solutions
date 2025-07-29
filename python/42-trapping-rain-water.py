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


s = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s.trap(height)


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
