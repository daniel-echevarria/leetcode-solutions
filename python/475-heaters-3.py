import bisect


class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        heaters.sort()
        min_radius = 0

        for h in houses:
            idx = bisect.bisect(heaters, h)
            if idx == 0:
                min_radius = max(min_radius, heaters[idx] - h)
            elif idx == len(heaters):
                min_radius = max(min_radius, h - heaters[idx - 1])
            else:
                closest = min(h - heaters[idx - 1], heaters[idx] - h)
                min_radius = max(min_radius, closest)

        return min_radius


houses = [1, 2, 3, 4]
heaters = [1, 4]

s = Solution()
print(s.findRadius(houses, heaters))
