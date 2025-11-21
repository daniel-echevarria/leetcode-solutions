class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0

        memo = [False] * (amount + 1)

        for coin in coins:
            if coin > amount:
                continue
            memo[coin] = 1

        def dp(num):
            if memo[num]:
                return memo[num]
            min_steps = []
            for coin in coins:
                if num - coin > 0 and memo[num - coin]:
                    min_steps.append(memo[num - coin])
            if min_steps:
                return min(min_steps) + 1
            return False

        for i in range(1, amount + 1):
            memo[i] = dp(i)

        return memo[amount] or -1


coins = [1, 2, 5]
amount = 11
# coins = [3]
# amount = 4
s = Solution()
print(s.coinChange(coins, amount))


# Algorithm:
# Declare a memo of size amount with each value being False
# Then add the base cases by iterating through the coins and giving
# That key in the memo a value of 1
# Then iterate from 1 to the amount
# If the current value is in the memo return that
# Otherwise check for each possible coins we came what is the minimum
# we could have and add 1
# if there was no coin that could reach it justs stays false
# return memo[amount]
