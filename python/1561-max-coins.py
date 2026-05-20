class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        n = len(piles)
        third = int(n / 3)
        piles = sorted(piles, reverse=True)[:-third]
        return sum(piles[1::2])


piles = [2, 4, 1, 2, 7, 8]
s = Solution()
print(s.maxCoins(piles))
