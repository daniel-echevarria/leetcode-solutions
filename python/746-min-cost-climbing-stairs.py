class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        min_costs = [0] * n
        min_costs[0] = cost[0]
        min_costs[1] = cost[1]
        for i in range(2, n):
            min_costs[i] = min(min_costs[i - 1], min_costs[i - 2]) + cost[i]

        return min(min_costs[n - 1], min_costs[n - 2])


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        a, b = cost[0], cost[1]
        for i in range(2, n):
            a, b = b, min(a, b) + cost[i]
        return min(a, b)


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
s = Solution()
print(s.minCostClimbingStairs(cost))
