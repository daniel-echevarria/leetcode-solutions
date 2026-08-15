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


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""

        def calculateMax(i, j):
            nonlocal res
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > len(res):
                    res = s[i : j + 1]
                i -= 1
                j += 1

        for i in range(n):
            calculateMax(i, i)
            calculateMax(i, i + 1)
        return res


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        res = ""

        def calculateLongest(i, j):
            nonlocal res
            while i >= 0 and j < n and s[i] == s[j]:
                # the plus one is to count single letters
                if j - i + 1 > len(res):
                    res = s[i : j + 1]
                i -= 1
                j += 1

        for i in range(n):
            calculateLongest(i, i)
            calculateLongest(i, i + 1)

        return res


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""

        def checkLongest(i, j):
            nonlocal res
            while i >= 0 and j < n and s[i] == s[j]:
                if j - i + 1 > len(res):
                    res = s[i : j + 1]
                i -= 1
                j += 1

        for i in range(n):
            checkLongest(i, i)
            checkLongest(i, i + 1)

        return res


st = "babad"
s = Solution()
print(s.longestPalindrome(st))
