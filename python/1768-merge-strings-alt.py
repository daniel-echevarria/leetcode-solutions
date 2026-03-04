class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)

        i = 0

        res = []
        while i < m and i < n:
            res.append(word1[i])
            res.append(word2[i])
            i += 1

        res.append(word1[i:])
        res.append(word2[i:])

        return "".join(res)


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)

        res = []
        for a, b in zip(word1, word2):
            res.extend([a, b])
        return "".join(res) + word1[n:] + word2[m:]


s = Solution()
word1 = "abcde"
word2 = "pq"
print(s.mergeAlternately(word1, word2))


# Algo
# iterate through the smallest string
# pushing on char from each at each turn
# then append what's left of the bigger string
