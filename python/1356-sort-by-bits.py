import math


class Solution:
    def sortBB(self, num):
        return (bin(num)[2:]).count("1")

    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort(key=self.sortBB)
        return arr
        print(arr)


s = Solution()
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(s.sortByBits(arr))
