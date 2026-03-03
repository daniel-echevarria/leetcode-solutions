class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        memo = {}

        def dp(i, holding=False, transactions_left=k):
            if not transactions_left or i >= len(prices):
                return 0

            if (i, holding, transactions_left) in memo:
                return memo[(i, holding, transactions_left)]

            # skip day
            best = dp(i + 1, holding, transactions_left)

            # sell_today
            if holding:
                best = max(best, prices[i] + dp(i + 1, False, transactions_left - 1))
            else:
                best = max(best, -prices[i] + dp(i + 1, True, transactions_left))

            memo[(i, holding, transactions_left)] = best
            return best

        return dp(0)


s = Solution()
prices = [2, 4, 1]
k = 2

print(s.maxProfit(k, prices))
