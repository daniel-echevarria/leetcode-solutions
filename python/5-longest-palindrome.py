class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        memo = [[None] * n for _ in range(n)]

        def isPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    memo[l][r] = -1
                    return False
                l += 1
                r -= 1
            return True

        for length in range(n, 0, -1):
            for i in range(0, n - length + 1):
                j = i + length - 1

                if memo[i][j] is not None:
                    continue

                if isPalindrome(i, j):
                    return s[i : j + 1]
