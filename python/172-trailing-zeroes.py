class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 1:
            return 1
        return n * self.trailingZeroes(n - 1)


s = Solution()
print(s.trailingZeroes(100))

# Brute force algo
# Get the value of the factorial, count the 0 in the result string
# STACK OVERLOAD

# Pattern algo
