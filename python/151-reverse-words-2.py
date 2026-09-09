class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


class Solution:
    def reverseWords(self, s: str) -> str:
        a = "cool"
        s[:1] = a
        print(s)


st = "a good   example"
s = Solution()
print(s.reverseWords(st))
