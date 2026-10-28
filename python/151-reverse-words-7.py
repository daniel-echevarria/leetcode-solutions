class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s.strip())
        n = len(chars)

        def reverse(l, r):
            while l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1

        reverse(0, n - 1)

        start = end = 0
        while end < n:
            while end < n and chars[end] != " ":
                end += 1

            reverse(start, end - 1)

            while end < n and chars[end] == " ":
                chars[end] = ""
                end += 1

            start = end
            if end != n:
                chars[end - 1] = " "
        return "".join(chars)


# st = "the sky is blue"
st = "a good   example"

s = Solution()
print(s.reverseWords(st))
