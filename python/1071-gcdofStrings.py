import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        while str1 and str2:
            if len(str1) > len(str2):
                str1, str2 = str2, str1
            if str1 != str2[: len(str1)]:
                return ""
            str2 = str2[len(str1) :]
        if not str1:
            return str2
        return str1


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[: math.gcd(len(str1), len(str2))]


s = Solution()
str1 = "ABABAB"
str2 = "ABAB"

# str1 = "LEET"
# str2 = "CODE"


print(s.gcdOfStrings(str1, str2))


# Algo
# find the shortest string
# so long as the shortest string is in the bigger string
# remove the shorter from the bigger
# if at some point is not possible to remove anymore return enmpty string
# if the longest is an empty string
# return the shortest
