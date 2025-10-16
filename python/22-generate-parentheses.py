class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        results = []

        def backtrack(path, a, b):
            if len(path) == n * 2:
                results.append(path)
                return
            if a < n:
                backtrack(path + "(", a + 1, b)
            if b < a:
                backtrack(path + ")", a, b + 1)

        backtrack("(", 1, 0)
        return results


s = Solution()
s.generateParenthesis(3)
