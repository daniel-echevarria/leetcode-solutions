class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repetitions = 1
        a_copy = a
        if b in a:
            return repetitions
        if len(a) > len(b):
            if b in (a + a):
                return 2
        while len(a) <= len(b) * 2:
            a += a_copy
            repetitions += 1
            if b in a:
                return repetitions
        return -1


s = Solution()
# a = "abcd"
# b = "cdabcdab"
a = "abc"
b = "cabcabca"
print(s.repeatedStringMatch(a, b))

# Algo
# As long as a is not 3 times bigger than b
# keep looping while adding a to a
# if at any point b is in a, return true
# after loop return false
