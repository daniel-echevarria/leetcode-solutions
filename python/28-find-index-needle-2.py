class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay_len = len(haystack)
        nee_len = len(needle)

        for i in range(hay_len):
            h, n = i, 0
            while h < hay_len and n < nee_len and haystack[h] == needle[n]:
                h += 1
                n += 1
            if n == nee_len:
                return i
        return -1
