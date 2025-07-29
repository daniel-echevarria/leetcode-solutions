from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        L = 0
        R = n
        shortest_sub = s

        def gen_s_letter_indexes():
            letter_indexes = defaultdict(list)
            for i in range(m):
                letter = s[i]
                letter_indexes[letter].append(i)
            return letter_indexes

        def gen_t_letter_count():
            letter_count = defaultdict(int)
            for i in range(n):
                letter = t[i]
                letter_count[letter] += 1
            return letter_count

        def isSubstring(l, r, sIndexes, tCounts):
            for pair in tCounts:
                letter, count = pair
                available = sum(1 for i in sIndexes[letter] if i >= l and i < r)
                if available < count:
                    return False
            return True

        s_letter_indexes = gen_s_letter_indexes()
        t_letter_count = gen_t_letter_count()

        result = isSubstring(0, 10, s_letter_indexes, t_letter_count.items())
        print(result)


sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
sol.minWindow(s, t)

# Algo
# Declare the variables L, R, shortestSub
# L gets 0, R gets t length
# shortestSub gets s
# Declare a method isSubstring that returns true if all the characters (including duplicates)
# Are present in the string
# Launch a loop that runs until L equals s length - n
# If the window between L and R is a substring
# compare the size to the shortest string so far
# If it's smaller, update the the shortestSub
# L gets +1
# If it's not a substring
# if  R equals m - 1 break
# R gets + 1
# return shortestSub

# isSubstring:
# Given a map of all the indexes for each letter
# Check if there is enough copies of the letters within the given window
