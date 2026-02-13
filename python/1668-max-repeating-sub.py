class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        temp, res = word, 0
        while temp in sequence:
            temp += word
            res += 1
        return res


s = Solution()
sequence = "ababc"
word = "ab"
print(s.maxRepeating(sequence, word))
