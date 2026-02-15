class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        min_days = float("inf")
        for i in range(k):
            harvest = []
            j = i
            while j <= len(bloomDay) - k:
                bouquet = bloomDay[j : j + k]
                harvest.append(max(bouquet))
                j += k
            if len(harvest) < m:
                continue
            harvest.sort()
            min_days = min(min_days, harvest[m - 1])
        return min_days


class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        sorted_blooms = sorted(list(set(bloomDay)))
        early_bloom, late_bloom = 0, len(sorted_blooms) - 1

        def can_make_bouquet(days):
            flowers = 0
            bouquets = 0
            for d in bloomDay:
                if d <= days:
                    flowers += 1
                else:
                    flowers = 0
                if flowers >= k:
                    bouquets += 1
                    flowers = 0
            return bouquets >= m

        while early_bloom < late_bloom:
            mid = (early_bloom + late_bloom) // 2
            if can_make_bouquet(sorted_blooms[mid]):
                late_bloom = mid
            else:
                early_bloom = mid + 1

        return (
            sorted_blooms[early_bloom]
            if can_make_bouquet(sorted_blooms[early_bloom])
            else -1
        )


class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        sorted_days = sorted(list(set(bloomDay)))
        l, r = 0, len(sorted_days) - 1

        def can_make_bouquets(num_days):
            flowers = 0
            bouquets = 0
            for d in bloomDay:
                if d <= num_days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        while l < r:
            mid = (l + r) // 2
            if can_make_bouquets(sorted_days[mid]):
                r = mid
            else:
                l = mid + 1

        return sorted_days[l] if can_make_bouquets(sorted_days[l]) else -1


# bloomDay = [1, 10, 3, 10, 2]
# m = 3
# k = 1
bloomDay = [7, 7, 7, 7, 12, 7, 7]
m = 2
k = 3

s = Solution()
print(s.minDays(bloomDay, m, k))
