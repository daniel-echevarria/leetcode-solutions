class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        min_count = float("inf")

        def helper(w1, w2, count=0):
            n, m = len(w1), len(w2)
            if w1 in w2 or w2 in w1:
                min_count = min(min_count, count + abs(n, m))

            for i in range(n):
                if n > m:
                    helper(w1[i + 1 :], w2, count + 1)
                    helper(w2[i] + w1[i + 1 :], w2, count + 1)
                else:
                    helper(w2[i] + w1[i + 1 :], w2, count + 1)
                    helper(w2[i] + w1, w2, count + 1)

        helper(word1, word2)

        return min_count


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word1, word2 = word2, word1

        min_distance = float("inf")

        def helper(w1, w2, count=0):
            nonlocal min_distance
            if not w1:
                min_distance = min(min_distance, count + len(w2))
                return
            if not w2:
                min_distance = min(min_distance, count + len(w1))
                return

            if w1[0] == w2[0]:
                helper(w1[1:], w2[1:], count)

            # replace
            helper(w1[1:], w2[1:], count + 1)
            # insert
            helper(w1, w2[1:], count + 1)
            # delelte
            helper(w1[1:], w2, count + 1)

        helper(word1, word2)

        return min_distance


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        m, n = len(word1), len(word2)

        def dp(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                ans = dp(i + 1, j + 1)
            else:
                ans = 1 + min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1))

            memo[i, j] = ans
            return ans

        return dp(0, 0)


s = Solution()
word1 = "horse"
word2 = "ros"
print(s.minDistance(word1, word2))

# Given two words return the min number of operations to transform word one into word2
# The three possible operations are:
# Delete char
# insert char
# replace char

# ALGO:
# Declare a helper function that takes two strings
# if word2 is a part of word1
# we can return the current count + the difference of length
# if the word1 is part of word 2
# we can return the current count + the difference of length
# otherwise we iterate through the char of word1
# and launch iteration, in the case word1 is bigger than word2:
# we just try delete or replace
# in the case word1 is smaller we just replace or insert
