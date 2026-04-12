class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:

        res = []
        path = []

        def backtrack(start, total):
            if len(path) == k:
                if total == n:
                    res.append(path.copy())
                return

            for j in range(start, 10):
                if total + j > n:
                    break
                path.append(j)
                backtrack(j + 1, total + j)
                path.pop()

        backtrack(1, 0)
        return res


k = 3
n = 9

s = Solution()
print(s.combinationSum3(k, n))
