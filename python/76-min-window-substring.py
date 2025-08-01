from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        L = 0
        shortest_sub = (-1, -1)
        shortest_len = float("inf")
        t_counts = Counter(t)
        window_counts = Counter()
        have, need = 0, len(t_counts)
        for R in range(len(s)):
            r_char = s[R]
            window_counts[r_char] += 1
            if r_char in t_counts and t_counts[r_char] == window_counts[r_char]:
                have += 1
            while have == need:
                if R - L + 1 < shortest_len:
                    shortest_sub = (L, R)
                    shortest_len = R - L + 1
                l_char = s[L]
                window_counts[l_char] -= 1
                L += 1
                if l_char in t_counts and t_counts[l_char] > window_counts[l_char]:
                    have -= 1
        l, r = shortest_sub
        res = s[l : r + 1]
        return res


s = "ADOBECODEBANC"
t = "gg"
sol = Solution()
sol.minWindow(s, t)
