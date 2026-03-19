from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())


# word1 = "abc"
# word2 = "bca"
word1 = "a"
word2 = "aa"

s = Solution()
print(s.closeStrings(word1, word2))
