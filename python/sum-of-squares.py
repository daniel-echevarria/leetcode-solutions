import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, math.isqrt(c)
        while l <= r:
            curr = l * l + r * r
            if curr == c:
                return True
            if curr > c:
                r -= 1
            if curr < c:
                l += 1
        return False


s = Solution()
print(s.judgeSquareSum(8))
