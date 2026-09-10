class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        s = list(s[::-1])

        l = 0
        while l < n - 1:
            if s[l] == " ":
                if l > 0 and s[l - 1] == " " or s[l - 1] == "":
                    s[l] = ""
                l += 1
                continue
            r = l
            while r < n and s[r].isalnum():
                r += 1
            i = r - 1
            while i > l:
                s[l], s[i] = s[i], s[l]
                i -= 1
                l += 1
            l = r + 1

        return "".join(s).strip()


# st = "the sky is blue"
# st = "  hello world  "
st = "a good   example"
s = Solution()
print(s.reverseWords(st))
