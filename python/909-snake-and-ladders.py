class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        gameBoard = [list(range(n)) for _ in range(n)]
        square_num = 1
        for row in range(n):
            for col in range(n):
                gameBoard[row][col] = square_num
                square_num += 1
        for row in range(n):
            if row % 2 != 0:
                gameBoard[row].reverse()


s = Solution()
s.snakesAndLadders(
    [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]
)


# Iterate through the board and change the values to the numbers
