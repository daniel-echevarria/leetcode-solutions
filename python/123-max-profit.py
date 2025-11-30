from operator import itemgetter


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # tuple model is sum, holding, transactions_count, profit
        memo = [[] for _ in range(len(prices) + 1)]
        memo[0].append((0, False, 0, 0))

        for i, p in enumerate(prices):
            for state in memo[i]:
                c, h, t_count, profit = state

                if t_count == 2:
                    memo[i + 1].append((c, h, t_count, profit))
                elif h:
                    new_profit = profit + p - c
                    memo[i + 1].append((0, False, t_count + 1, new_profit))
                    memo[i + 1].append((c, h, t_count, profit))
                else:
                    memo[i + 1].append((p, True, t_count, profit))
                    memo[i + 1].append((c, h, t_count, profit))
        return max(memo[-1], key=itemgetter(3))[3]


s = Solution()
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(s.maxProfit(prices))
