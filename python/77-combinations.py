class Solution:

    def combine(self, n: int, k: int) -> list[list[int]]:
        results = []

        def backtrack(n, k, path=[], current=0):
            if len(path) == k:
                results.append(path)
                return
            for i in range(current, n):
                backtrack(n, k, [*path, i + 1], i + 1)

        backtrack(n, k)
        return results


s = Solution()
print(s.combine(4, 2))
