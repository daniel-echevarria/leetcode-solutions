class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        for i in range(c + 1):
            if i * i == c:
                return True
            if c - i * i in squares:
                return True
            if i * i * 2 == c:
                return True
            squares.add(i * i)
        return False


s = Solution()
print(s.judgeSquareSum(2))
