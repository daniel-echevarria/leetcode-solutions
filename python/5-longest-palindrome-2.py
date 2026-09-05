class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""

        def expand(i, j):
            nonlocal longest
            while i >= 0 and j <= n - 1 and s[i] == s[j]:
                if j - i + 1 > len(longest):
                    longest = s[i : j + 1]
                i -= 1
                j += 1

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        return longest
