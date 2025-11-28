class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        n, m = len(matrix), len(matrix[0])

        max_square = 0

        matrix = [[int(val) for val in row] for row in matrix]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] > 0:
                    if i > 0 and j > 0:
                        top = matrix[i - 1][j]
                        left = matrix[i][j - 1]
                        diag = matrix[i - 1][j - 1]
                        matrix[i][j] = min(top, left, diag) + 1
                    max_square = max(max_square, matrix[i][j])

        return max_square * max_square


s = Solution()
# matrix = [
#     ["1", "0", "1", "0", "0"],
#     ["1", "0", "1", "1", "1"],
#     ["1", "1", "1", "1", "1"],
#     ["1", "0", "1", "1", "1"],
# ]
# matrix = [["1", "1"]]
matrix = [["0", "1"], ["1", "0"]]
print(s.maximalSquare(matrix))

# Algo:
# Iterate through the square:
# if the square is a 0, continue
# if the upper, left and diagonal are bigger than 0
# this square gets the min of the neighbors + 1
# return the max value squared
