class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backtrack(y, x, k):
            if not (0 <= x < n and 0 <= y < m):
                return
            if board[y][x] != word[k]:
                return
            if k == len(word) - 1:
                return True

            tmp = board[y][x]
            board[y][x] = "#"

            found = (
                backtrack(y, x - 1, k + 1)
                or backtrack(y, x + 1, k + 1)
                or backtrack(y + 1, x, k + 1)
                or backtrack(y - 1, x, k + 1)
            )
            board[y][x] = tmp
            return found

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False
