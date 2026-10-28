class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = end = 0

        def expand(i, j):
            nonlocal start, end
            while i >= 0 and j < n and s[i] == s[j]:
                if j - i > end - start:
                    end, start = j, i
                i -= 1
                j += 1

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)

        return s[start : end + 1]
