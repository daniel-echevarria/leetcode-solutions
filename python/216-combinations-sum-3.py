class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:

        res = []
        path = []

        def backtrack(i):
            if len(path) == k:
                if sum(path) == n:
                    res.append(path.copy())
                return
            for j in range(i + 1, 10):
                path.append(j)
                backtrack(j)
                path.pop()

        backtrack(0)
        return res


k = 3
n = 9

s = Solution()
print(s.combinationSum3(k, n))
