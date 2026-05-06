from collections import defaultdict


class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        counts = defaultdict(int)
        res = []
        total = 0
        for a, b in zip(A, B):
            counts[a] += 1
            if counts[a] == 2:
                total += 1

            counts[b] += 1
            if counts[b] == 2:
                total += 1

            res.append(total)

        return res


A = [1, 3, 2, 4]
B = [3, 1, 2, 4]

Output: [0, 2, 3, 4]

s = Solution()
print(s.findThePrefixCommonArray(A, B))
