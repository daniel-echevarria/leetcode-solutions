class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)

        for i in range(h_len):
            h, n = i, 0
            while h < h_len and n < n_len and haystack[h] == needle[n]:
                h += 1
                n += 1
            if n == n_len:
                return i
        return -1
