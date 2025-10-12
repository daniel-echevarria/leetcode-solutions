class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start, path, moves, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(moves)):
                backtrack(
                    i, path=[*path, moves[i]], moves=moves, total=total + moves[i]
                )

        backtrack(0, [], candidates, 0)
        print(result)
        return result


s = Solution()
s.combinationSum([2, 3, 5], 8)
