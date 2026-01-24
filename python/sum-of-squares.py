class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, c / 2
        while l < r:
            curr = l * l + r * r
            if curr == c:
                return True


s = Solution()
print(s.judgeSquareSum(2))
