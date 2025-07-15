class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        really_visited = set()
        pairs = []

        def restore():
            for pair in pairs:
                i, j = pair
                board[i][j] = 'O'
                really_visited.add(f"{i}#{j}")

        def isOutOfBounds(i, j):
            if i < 0 or j < 0 or i > m - 1 or j > n - 1:
                return True
            return False

        def isRegion(i, j):
            coordinate_string = f"{i}#{j}"
            if isOutOfBounds(i, j) or coordinate_string in really_visited:
                return False
            if board[i][j] == 'X':
                return True
            pairs.append([i, j])
            board[i][j] = 'X'
            return isRegion(i + 1, j) and isRegion(i - 1, j) and isRegion(i, j + 1) and isRegion(i, j - 1)

        for i in range(m):
            for j in range(n):
                pairs = []
                coordinate_string = f"{i}#{j}"
                if board[i][j] == 'X' or coordinate_string in really_visited:
                    continue
                if not isRegion(i, j):
                    restore()



s = Solution()
s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])

# Iterate through the matrix
# if the value is X, continue
# if the value is O, look if the region is surrounded (no neighbor is out of bounds)
# if it is call dfs again to capture the region
