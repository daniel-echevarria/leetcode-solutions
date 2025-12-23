class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        divider = 2
        while divider <= n:
            quotient, rest = divmod(n, divider)
            if rest == 0:
                if s[:quotient] * divider == s:
                    return True
            divider += 1
        return False


s = Solution()
st = "abcabcabcabcf"
print(s.repeatedSubstringPattern(st))


# Starting with 2,
# use divmod
# launch a loop that for a given number checks if the rest of modulo is 0
# if it is check if multiplying a string of length from the number
# by the quotient, gives the initial string, if it does return true
# add one to the starting number
# if the starting number is bigger than the length of s
# return false
