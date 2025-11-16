class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, abs(n))
        if x == 0:
            return 0
        if n == 0:
            return 1

        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        else:
            return x * self.myPow(x, n - 1)


s = Solution()
# x = 0.0001
# n = 2147483647
# x = 2
# n = 3
x = 2
n = -2
print(s.myPow(x, n))
