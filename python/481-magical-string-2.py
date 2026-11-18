class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1

        start = [1, 2, 2]
        nxt = 1
        idx = 2

        while len(start) < n:
            last = start[idx]
            for _ in range(last):
                start.append(nxt)
            idx += 1
            nxt = 1 if nxt == 2 else 2

        return start[:n].count(1)


n = 8
s = Solution()
print(s.magicalString(n))
