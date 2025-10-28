class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        def helper(l, r, row):
            if not row[l] <= target <= row[r]:
                return
            if l == r:
                return row[l] == target
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                return helper(mid + 1, r, row)
            else:
                return helper(l, mid, row)

        for row in matrix:
            if helper(0, len(row) - 1, row):
                return True

        return False


s = Solution()
# matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# target = 4
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
target = 5
print(s.searchMatrix(matrix, target))
