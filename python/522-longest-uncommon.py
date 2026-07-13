class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        strs.sort(key=len, reverse=True)
        longest = 0
        n = len(strs)

        for i, s in enumerate(strs):
            for j in range(i + 1, n):
                k = l = 0
                while k < len(s) and l < len(strs[j]):
                    if s[k] == strs[j][l]:
                        k += 1
                    l += 1
                if k != len(s):
                    return len(s)
        return -1


class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        strs.sort(key=len, reverse=True)

        def is_sub(a, b):
            i = j = 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)

        for i, s in enumerate(strs):
            uncommon = True

            for j, t in enumerate(strs):
                if i == j:
                    continue

                if is_sub(s, t):
                    uncommon = False
                    break
            if uncommon:
                return len(s)

        return -1


strs = ["aba", "cdc", "eae"]
s = Solution()
print(s.findLUSlength(strs))
