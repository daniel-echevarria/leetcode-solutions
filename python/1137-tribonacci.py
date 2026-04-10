class Solution:
    def tribonacci(self, n: int) -> int:
        tribo = [0, 1, 1]
        tribo.extend([0] * (n - 2))
        for i in range(3, n + 1):
            tribo[i] = sum(tribo[i - 3 : i])

        return tribo[n]


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return [0, 1, 1][n]

        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c


s = Solution()
print(s.tribonacci(25))
