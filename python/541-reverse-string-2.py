class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        l = r = 0
        n = len(s)
        while r < n:
            r += k
            res.append(s[l:r][::-1])
            l += k
            r += k
            res.append(s[l:r])
            l += k
        return "".join(res)


st = "abcdefg"
k = 2
s = Solution()
print(s.reverseStr(st, k))
