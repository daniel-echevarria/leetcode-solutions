class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:

s = Solution()
# prices = [8, 4, 6, 2, 3]
prices = [4, 7, 1, 9, 4, 8, 8, 9, 4]
print(s.finalPrices(prices))


# Algo
# Declare an empty stack, a result array and a temporary array
# Iterate through the prices
# If the stack is not empty:
# Iterate backwards from the top of the stack
# pop values if they are equal or smaller than the current
# add the price - the current price to the temporary
# after backwards iteration append the reverse array to the res
# after iteration add the stack to the result and append
