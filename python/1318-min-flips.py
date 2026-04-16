class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        while True:
            if a | b == c:
                return flips

            lastA = a & 1
            lastB = b & 1
            lastC = c & 1
            if lastC == 1:
                flips += 0 if lastA | lastB else 1
            else:
                if lastA & lastB:
                    flips += 2
                elif lastA | lastB:
                    flips += 1
                else:
                    "do nothing"
            a >>= 1
            b >>= 1
            c >>= 1


# a = 4
# b = 2
# c = 7
a = 2
b = 6
c = 5

s = Solution()
print(s.minFlips(a, b, c))
