class Solution:
    def numToCoordinates(self, num: int, board_size: int):
        row_from_bottom = (num - 1) // board_size
        row = board_size - 1 - row_from_bottom
        col = (num - 1) % board_size
        if row_from_bottom % 2 != 0:
            col = board_size - 1 - col
        print(row, col)
        return (row, col)

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        print("yo")


s = Solution()
s.numToCoordinates(13, 4)
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
