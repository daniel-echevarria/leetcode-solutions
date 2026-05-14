class SubrectangleQueries:

    def __init__(self, rectangle: list[list[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


subrectangleQueries = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
print(
    subrectangleQueries.getValue(0, 2),
    subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5),
    subrectangleQueries.getValue(0, 2),
    subrectangleQueries.getValue(3, 1),
    subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10),
    subrectangleQueries.getValue(3, 1),
    subrectangleQueries.getValue(0, 2),
)
