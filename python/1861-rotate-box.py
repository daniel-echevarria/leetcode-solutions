class Solution:
    def rotateRow(self, row):
        n = len(row)
        l = 0
        for r in range(l, n):
            if row[r] == "*":
                l = r + 1
                continue
            if row[r] == ".":
                row[l], row[r] = row[r], row[l]
                l += 1

        return row

    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        res = [[0] * m for _ in range(n)]
        for row in boxGrid:
            self.rotateRow(row)
        for i in range(m):
            for j in range(n):
                res[j][i] = boxGrid[i][j]
        for row in res:
            row.reverse()
        return res


boxGrid = [
    ["#", "#", "*", ".", "*", "."],
    ["#", "#", "#", "*", ".", "."],
    ["#", "#", "#", ".", "#", "."],
]

s = Solution()
print(s.rotateTheBox(boxGrid))

# Algo on each row, track a left and right pointer
# loop until the left pointer matches the length of the row
# inside the loop, move the left pointer to the next stone
# then from there move the right pointer
# if the right pointer finds a empty slot, swap with left pointer
# and move both pointers to the next round
# if meet with a wall, move both pointers to the next
# do that for all rows
