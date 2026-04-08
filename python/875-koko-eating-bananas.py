class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid
            if hours <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l


# piles = [3, 6, 7, 11]
piles = [30, 11, 23, 4, 20]
h = 6
s = Solution()
print(s.minEatingSpeed(piles, h))
