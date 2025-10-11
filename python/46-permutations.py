class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(path=[], moves=nums):
            if len(path) == len(nums):
                result.append(path)
                return
            for i in range(len(moves)):
                backtrack(
                    [*path, moves[i]],
                    [*moves[:i], *moves[i + 1 :]],
                )

        backtrack()
        return result


s = Solution()
s.permute([4, 7, 9])
