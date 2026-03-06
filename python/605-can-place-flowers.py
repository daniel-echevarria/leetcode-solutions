class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        planted_flowers = 0

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                planted_flowers += 1
                flowerbed[i] = 1

        return planted_flowers >= n


s = Solution()
# flowerbed = [1, 0, 0, 0, 0, 0, 1]
flowerbed = [1, 0, 0, 0, 1, 0, 0]
n = 2
print(s.canPlaceFlowers(flowerbed, n))


# iterate through the flower from index one,
# if the current value is 0 and the previous value is also 0
# add a flower to the current plot, flowers to plant get -1
# if the current value is 1 and the previous value is also 1
# remove the flower from the previous plot, flower to plant gets + 1
# return weather flower to plant is bigger than 0
