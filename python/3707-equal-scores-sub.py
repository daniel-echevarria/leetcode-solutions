from itertools import accumulate


class Solution:
    def scoreBalance(self, s: str) -> bool:
        prefix = list(accumulate([ord(char) - 96 for char in s]))
        total = prefix[-1]
        return True if total / 2 in prefix else False


st = "adcb"
s = Solution()
print(s.scoreBalance(st))
