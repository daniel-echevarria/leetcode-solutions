class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        max_profit = 0

        def helper(idx, holding, profit):
            nonlocal max_profit
            if idx == n:
                max_profit = max(profit, max_profit)
                return
            if holding:
                helper(idx + 1, False, profit + prices[idx] - fee)
                helper(idx + 1, True, profit)
            else:
                helper(idx + 1, True, profit - prices[idx])
                helper(idx + 1, False, profit)

        helper(0, False, 0)
        return max_profit


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        dp = [0] * n + 1
        for i in range(1, len(dp)):
            dp[i] = max


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        hold = -prices[0]
        profit = 0

        for p in range(1, len(prices)):
            hold = max(hold, profit - prices[p])
            profit = max(profit, hold + prices[p] - fee)
        return profit


# prices = [1, 3, 2, 8, 4, 9]
# fee = 2
prices = [1, 3, 7, 5, 10, 3]
fee = 3

s = Solution()
print(s.maxProfit(prices, fee))
