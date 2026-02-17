class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        l = r = 0
        counts = {}
        results = 0
        while r < n:
            while not ("a" in counts and "b" in counts and "c" in counts) and r < n:
                counts[s[r]] = counts.get(s[r], 0) + 1
                r += 1
            while "a" in counts and "b" in counts and "c" in counts:
                results += n - r + 1
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    del counts[s[l]]
                l += 1
        return results


s = Solution()
# st = "abcabc"
# st = "aaacb"
st = "abab"
print(s.numberOfSubstrings(st))
