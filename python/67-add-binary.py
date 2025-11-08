class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), "b")


s = Solution()
a = "1010"
b = "1110"
print(s.addBinary(a, b))
