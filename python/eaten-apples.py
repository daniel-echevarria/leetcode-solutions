import heapq


class Solution:
    def eatenApples(self, apples: list[int], days: list[int]) -> int:
        apples_stock = []
        heapq.heapify(apples_stock)
        apples_eaten = 0
        current_day = 0
        for i, d in enumerate(days):
            heapq.heappush(apples_stock, ((d + i), apples[i]))
            ate_apple = False
            current_day = i
            while apples_stock and not ate_apple:
                rot, app = heapq.heappop(apples_stock)
                if rot <= current_day or app < 1:
                    continue
                apples_eaten += 1
                app -= 1
                ate_apple = True
                heapq.heappush(apples_stock, (rot, app))
        current_day += 1
        while apples_stock:
            rot, app = heapq.heappop(apples_stock)
            if rot <= current_day or app < 1:
                continue
            current_day += 1
            apples_eaten += 1
            app -= 1
            heapq.heappush(apples_stock, (rot, app))

        return apples_eaten


s = Solution()
apples = [1, 2, 3, 5, 2]
days = [3, 2, 1, 4, 2]
# apples = [3, 0, 0, 0, 0, 2]
# days = [3, 0, 0, 0, 0, 2]
# apples = [2, 1, 1, 4, 5]
# days = [10, 10, 6, 4, 2]


print(s.eatenApples(apples, days))

# Algo:
# Iterate through the days keeping track of the idx and values
# add to a heap (stock of apples) the combination of the apples and the day they will rot
# Keep track of the eaten apples
# after iterating keep eating apples until the heap is empty
