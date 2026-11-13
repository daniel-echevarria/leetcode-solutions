class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        i = j = 0

        while i < n and j < m:
            while j < m and t[j] != s[i]:
                j += 1

            if j == m:
                break

            i += 1
            j += 1

        return i == n


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        i = 0

        for char in t:
            if i < n and s[i] == char:
                i += 1

        return i == n
