class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> list[list[int]]:
        side_size = 0
        current_position = [rStart, cStart]
        res = [current_position]

        while len(res) < rows * cols:
            spiral = []
            side_size += 1
            # Move right
            for _ in range(1, side_size + 1):
                cStart += 1
                spiral.append([rStart, cStart])
            # Move down
            for _ in range(1, side_size + 1):
                rStart += 1
                spiral.append([rStart, cStart])
            side_size += 1
            # Move Left
            for _ in range(1, side_size + 1):
                cStart -= 1
                spiral.append([rStart, cStart])
            # Move up
            for _ in range(1, side_size + 1):
                rStart -= 1
                spiral.append([rStart, cStart])
            for [x, y] in spiral:
                if 0 <= x < rows and 0 <= y < cols:
                    res.append([x, y])

        return res


rows = 1
cols = 4
rStart = 0
cStart = 0

s = Solution()
print(s.spiralMatrixIII(rows, cols, rStart, cStart))


# Algo
# Sides size happend by group of two, starting with one, move the side size to the right then down
# then add one to the side size, move left and up, add one, move right and down etc.
# if we are outside of the grid, just continue, otherwise add the coordinate to the result
# stop when the length of the result is the same than the grid
