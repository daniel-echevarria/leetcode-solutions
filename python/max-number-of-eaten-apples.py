import heapq


class Solution:
    def eatenApples(self, apples: list[int], days: list[int]) -> int:
        n = len(apples)
        current_day = 0
        apples_eaten = 0
        heap = [(days[0], apples[0])]
        while heap:
            while heap:
                day_rotten, apls = heapq.heappop(heap)
                if day_rotten > current_day and apls > 0:
                    apples_eaten += 1
                    left_apples = apls - 1
                    if left_apples:
                        heapq.heappush(heap, (day_rotten, left_apples))
                    break
            current_day += 1
            if current_day < n:
                heapq.heappush(
                    heap, (days[current_day] + current_day, apples[current_day])
                )
        return apples_eaten


s = Solution()
apples = [1, 2, 3, 5, 2]
days = [3, 2, 1, 4, 2]
# apples = [3, 0, 0, 0, 0, 2]
# days = [3, 0, 0, 0, 0, 2]
# apples = [2, 1, 10]
# days = [2, 10, 1]

print(s.eatenApples(apples, days))
