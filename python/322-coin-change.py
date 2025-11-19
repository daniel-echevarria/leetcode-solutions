class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = [float("inf")]

        coins.sort(reverse=True)
        print(coins)

        def dfs(num, count=0):
            if num == 0:
                memo[num] = min(memo[num], count)
                return True
            if num < 0:
                return False
            for coin in coins:
                if dfs(num - coin, count + 1):
                    return

        dfs(amount)
        return -1 if memo[0] == float("inf") else memo[0]


s = Solution()
coins = [1, 2, 5]
amount = 11
# coins = [2]
# amount = 3
print(s.coinChange(coins, amount))

# Algo, given a number
# Declare a variable memo with an initial value of an empty dict
# Recursively iterate through the coins
