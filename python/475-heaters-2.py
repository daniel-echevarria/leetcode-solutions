from bisect import bisect_left


class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        heaters.sort()
        min_radius = 0
        m, n = len(houses), len(heaters)

        for house in houses:
            pos = bisect_left(heaters, house)
            radius = min_radius
            if pos == 0:
                radius = heaters[0] - house
            elif pos == n:
                radius = house - heaters[n - 1]
            else:
                radius = min(house - heaters[pos - 1], heaters[pos] - house)
            min_radius = max(min_radius, radius)
        return min_radius


houses = [1, 2, 3, 4]
heaters = [1, 4]
# houses = [1, 2, 3]
# heaters = [2]
s = Solution()
print(s.findRadius(houses, heaters))
