class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        r = len(s) - 1
        open_brak = 0
        clos_brak = 0
        swaps = 0
        for l, char in enumerate(s):
            if char == "[":
                open_brak += 1
            else:
                clos_brak += 1
            if clos_brak > open_brak:
                while s[r] != "[":
                    r -= 1
                s[l], s[r] = s[r], s[l]
                open_brak += 1
                clos_brak -= 1
                swaps += 1
        return swaps


class Solution:
    def minSwaps(self, s: str) -> int:
        biggest_deep = 0
        depth = 0
        for c in s:
            if c == "]":
                depth += 1
            else:
                depth -= 1
            biggest_deep = max(biggest_deep, depth)

        return (biggest_deep + 1) // 2


st = "][]["
s = Solution()
print(s.minSwaps(st))
