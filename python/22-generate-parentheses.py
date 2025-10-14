class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        results = []
        count = {"(": 0, ")": 0}

        def backtrack(path, current):
            count[current] += 1
            if len(path) == n * 2:
                results.append(path)
                return
            if count[")"] < count["("]:
                backtrack(path + ")", current=")")
            if path.count("(") < n:
                print(path)
                backtrack(path + "(", current="(")

        backtrack("(", "(")
        print(results)


s = Solution()
s.generateParenthesis(3)
