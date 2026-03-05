class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res = []
        max_candies = max(candies)
        for c in candies:
            res.append(c + extraCandies >= max_candies)
        return res


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_c = max(candies)
        return list(map(lambda x: x + extraCandies >= max_c, candies))


# Algo, find the max candies
# iterate through the array and push true if the current number + the extra is bigger or equal to the max
# return the result array
