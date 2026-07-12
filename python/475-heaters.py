import bisect


class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        n = len(heaters)

        for h in houses:
            idx = bisect.bisect(heaters, h)
            if idx == 0:
                res = max(res, heaters[0] - h)
            elif idx == n:
                res = max(res, h - heaters[n - 1])
            else:
                res = max(res, min(h - heaters[idx - 1], heaters[idx] - h))
        return res


# houses = [1, 2, 3]
# heaters = [2]
# houses = [1, 5]
# heaters = [2]

houses = [1, 2, 3, 4]
heaters = [1, 4]

s = Solution()
print(s.findRadius(houses, heaters))
