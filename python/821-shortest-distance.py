class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        stack = []
        res = [n] * n
        for i, char in enumerate(s):
            if char != c:
                stack.append(i)
            else:
                res[i] = 0
                while stack:
                    j = stack.pop()
                    res[j] = min(res[j], abs(j - i))

        for i in range(n - 1, -1, -1):
            if s[i] != c:
                stack.append(i)
            else:
                while stack:
                    j = stack.pop()
                    res[j] = min(res[j], abs(j - i))
        return res


st = "loveleetcode"
c = "e"
s = Solution()
print(s.shortestToChar(st, c))
