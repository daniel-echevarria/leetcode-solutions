from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        L = 0
        R = n
        shortest_sub = ""

        def gen_s_letter_indexes():
            letter_indexes = defaultdict(list)
            for i in range(m):
                letter = s[i]
                if letter not in t:
                    continue
                letter_indexes[letter].append(i)
            return letter_indexes

        def gen_t_letter_count():
            letter_count = defaultdict(int)
            for i in range(n):
                letter = t[i]
                letter_count[letter] += 1
            return letter_count

        def isSubstring(l, r, sIndexes, tCounts):
            for pair in tCounts:
                letter, count = pair
                available = sum(1 for i in sIndexes[letter] if i >= l and i < r)
                if available < count:
                    return False
            return True

        s_letter_indexes = gen_s_letter_indexes()
        t_letter_count = gen_t_letter_count()

        while L < (m - n + 1):
            substring = s[L:R]
            if isSubstring(L, R, s_letter_indexes, t_letter_count.items()):
                if not shortest_sub or len(substring) < len(shortest_sub):
                    shortest_sub = substring
                L += 1
            else:
                if R == m:
                    break
                R += 1
        print(shortest_sub)
        return shortest_sub


sol = Solution()
s = "A"
t = "A"
sol.minWindow(s, t)
