class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        s1 = s1 * n1
        s2 = s2 * n2
        n = len(s1)
        m = len(s2)

        i = j = 0
        rounds = 0

        while i < n:
            if s1[i] == s2[j]:
                j += 1
            if j == m:
                j = 0
                rounds += 1
            i += 1
        return rounds


s1 = "acb"
n1 = 4
s2 = "ab"
n2 = 2

s = Solution()
print(s.getMaxRepetitions(s1, n1, s2, n2))
