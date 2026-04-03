import heapq


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        min_heap = []
        max_heap = []
        total_cost = 0
        for i, c in enumerate(costs):
            heapq.heappush(min_heap, (i, c))
            heapq.heappush(max_heap, (-i, c))
        while k:

            contest = []
            contest_set = set()
            for i in range(candidates):
                j, c = heapq.heappop(min_heap)
                cand = (c, j)
                if cand not in contest_set:
                    heapq.heappush(contest, (c, j))
                j, c = heapq.heappop(max_heap)
                cand = (c, -j)
                if cand not in contest_set:
                    heapq.heappush(contest, (c, j, "-"))
            round_winner = heapq.heappop(contest)
            total_cost += round_winner[0]
            k -= 1
            for challenger in contest:
                if len(challenger) == 2:
                    c, j = challenger
                    heapq.heappush(min_heap, (j, c))
                else:
                    c, j, sign = challenger
                    heapq.heappush(max_heap, (-j, c))
            print(round_winner)


# costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
# k = 3
# candidates = 4

costs = [1, 2, 4, 1]
k = 3
candidates = 3


s = Solution()
print(s.totalCost(costs, k, candidates))
