class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for row_i in range(1, len(triangle)):
            for col_i in range(len(triangle[row_i])):
                if col_i == 0:
                    triangle[row_i][col_i] += triangle[row_i - 1][col_i]
                elif col_i == len(triangle[row_i]) - 1:
                    triangle[row_i][col_i] += triangle[row_i - 1][col_i - 1]
                else:
                    triangle[row_i][col_i] += min(
                        triangle[row_i - 1][col_i - 1], triangle[row_i - 1][col_i]
                    )
        return min(triangle[-1])


tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
s = Solution()
print(s.minimumTotal(tri))

# Algo
# Iterate through the triangle from index 1
# for each row update the value with the minimum possible value to get there
# following this, if index is 0 just change it to the sum of the previous 0
# plus the current smae for last index, otherwise  current is the min of
# previous -1 + current or previous + current
# return the min of the last row
