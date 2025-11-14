class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            square = mid * mid
            next_square = (mid + 1) * (mid + 1)
            if square <= x and next_square > x:
                return mid
            elif square >= x:
                r = mid
            else:
                l = mid + 1


s = Solution()
print(s.mySqrt(1))

# Algo
# Declare two pointers l and r with initial value of 0 and of x
# Loop until l is bigger than r
# Each round check the middle value
# Compare it's square to x
# If it's bigger recurse the left half
# If it's smaller recurse the right half
