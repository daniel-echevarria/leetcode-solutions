class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # dp states:
        # buy1  = max profit after first buy
        # sell1 = max profit after first sell
        # buy2  = max profit after second buy
        # sell2 = max profit after second sell

        buy1 = float("-inf")
        sell1 = 0
        buy2 = float("-inf")
        sell2 = 0

        for price in prices:
            buy1 = max(buy1, -price)  # buy first stock
            sell1 = max(sell1, buy1 + price)  # sell first stock
            buy2 = max(buy2, sell1 - price)  # buy second stock
            sell2 = max(sell2, buy2 + price)  # sell second stock

        return sell2


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memo = {}

        def dp(i, active=False, transactions=2):
            if transactions == 0 or i == len(prices):
                return 0

            if (i, active, transactions) in memo:
                return memo[(i, active, transactions)]

            # skip today
            best_profit = dp(i + 1, active, transactions)

            if active:
                # sell_today
                best_profit = max(
                    best_profit, prices[i] + dp(i + 1, False, transactions - 1)
                )
            else:
                # buy_today
                best_profit = max(
                    best_profit, -prices[i] + dp(i + 1, True, transactions)
                )
            memo[(i, active, transactions)] = best_profit
            return best_profit

        return dp(0)


s = Solution()
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(s.maxProfit(prices))
