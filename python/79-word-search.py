class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        res = False

        def backtrack(y, x, path, board):
            nonlocal res
            if res:
                return
            if x < 0 or x > n - 1 or y < 0 or y > m - 1:
                return
            path += board[y][x]
            board[y][x] = "Done"
            if not word.startswith(path):
                return
            if path == word:
                res = True
                return
            backtrack(y, x - 1, path, board[:])
            backtrack(y, x + 1, path, board[:])
            backtrack(y + 1, x, path, board[:])
            backtrack(y - 1, x, path, board[:])

        for i in range(m):
            for j in range(n):
                backtrack(i, j, "", board[:])

        return res


s = Solution()
# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCCED"
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"

print(s.exist(board, word))
