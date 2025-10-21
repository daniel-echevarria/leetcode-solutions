class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0] * n for _ in range(n)]

        solutions = set()

        def backtrack(y, x, path="", i=[], j=[]):
            if len(path) == n * 3:
                solutions.add(path)
                return
            board[y][x] = "#"
            i.append(y)
            j.append(x)
            for k in range(n):
                for l in range(n):
                    if k in i or l in j:
                        continue
                    backtrack(k, l, path + f"{y},{x}", i, j)

        for y in range(n):
            for x in range(n):
                backtrack(y, x)


s = Solution()
print(s.totalNQueens(4))

# Algo
# Declare a valid path array
# iterate through all the squares in the the n * n matrix
# For each square attempt to make a placement from there
# recursing with the possible squares left and the current path
# when the length of the path is equal to n
# add the path to the valid path
#
