class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        if n == 1:
            return [1]

        return [2 * x - 1 for x in self.beautifulArray((n + 1) // 2)] + [
            2 * x for x in self.beautifulArray(n // 2)
        ]


s = Solution()
print(s.beautifulArray(7))
