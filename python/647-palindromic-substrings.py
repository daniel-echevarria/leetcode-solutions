class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def count_palindromes(i, j):
            if i < 0 or j > n - 1 or s[i] != s[j]:
                return 0
            return 1 + count_palindromes(i - 1, j + 1)

        for i in range(0, n):
            res += count_palindromes(i, i)
            res += count_palindromes(i, i + 1)

        return res


st = "aaa"
s = Solution()
print(s.countSubstrings(st))
