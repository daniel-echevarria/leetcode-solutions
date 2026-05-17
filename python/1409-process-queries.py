class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        res = []
        P = [x for x in range(1, m + 1)]
        for q in queries:
            idx = P.index(q)
            res.append(idx)
            P.insert(0, P.pop(idx))
        return res


queries = [3, 1, 2, 1]
m = 5
s = Solution()
print(s.processQueries(queries, m))
