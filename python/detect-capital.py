class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        low = word.lower()
        upp = word.upper()
        cap = upp[0] + low[1:]

        if word == low or word == upp or word == cap:
            return True
        return False


s = Solution()
print(s.detectCapitalUse("peaktime"))
