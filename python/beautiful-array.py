class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        if n == 1:
            return [1]

        odds = self.beautifulArray((n + 1) // 2)
        evens = self.beautifulArray(n // 2)

        result = []

        for x in odds:
            result.append(x * 2 - 1)

        for x in evens:
            result.append(x * 2)

        return result


s = Solution()
print(s.beautifulArray(7))
