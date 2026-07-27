from collections import defaultdict


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        counts = defaultdict(int)
        l, r = 0, 1
        prev = s[l]
        counts[prev] += 1

        res = 0
        while r < n:
            counts[s[r]] += 1
            if s[r] != prev:
                res += 1
                while s[l] == s[r]:
                    counts[s[l]] -= 1
                    l += 1
            else:
                if counts["0"] == counts["1"]:
                    res += 1
            prev = s[r]
            r += 1
        return res


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        zero_count = one_count = 0
        res = 0
        for char in s:
            if char == "1":
                if zero_count > 0:
                    res += 1
                    zero_count -= 1
                one_count += 1
            else:
                if one_count > 0:
                    res += 1
                    one_count -= 1
                zero_count += 1
        return res


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        z = o = 0
        res = 0
        n = len(s)
        while o < n and s[o] == "1":
            o += 1
        while z < n and s[z] == "0":
            z += 1
        while o < n and z < n:
            if s[o] != s[z]:
                res += 1
                o += 1
                z += 1


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        zero_p = one_p = 0
        n = len(s)
        res = 0
        while True:
            while zero_p < n and s[zero_p] != "0":
                zero_p += 1
            while one_p < n and s[one_p] != "1":
                one_p += 1
            if zero_p == n or one_p == n:
                res += abs(one_p - zero_p)
                return res
            res += 1
            zero_p += 1
            one_p += 1


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr = 1
        prev = 0
        res = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                res += min(prev, curr)
                prev = curr
                curr = 1
        return res + min(prev, curr)


st = "001110011"
# st = "10101"
# st = "000111000"
s = Solution()
print(s.countBinarySubstrings(st))
