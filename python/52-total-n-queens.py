class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        cols = set()
        pos_diago = set()
        neg_diago = set()

        def backtrack(r):
            if r == n:
                self.count += 1
                return
            for c in range(n):
                if c in cols or (r + c) in pos_diago or (r - c) in neg_diago:
                    continue
                cols.add(c)
                pos_diago.add(r + c)
                neg_diago.add(r - c)
                backtrack(r + 1)
                cols.remove(c)
                pos_diago.remove(r + c)
                neg_diago.remove(r - c)

        backtrack(0)
        return self.count


s = Solution()
print(s.totalNQueens(4))

# Algo
# Declare a valid path array
# iterate through all the squares in the the n * n matrix
# For each square attempt to make a placement from there
# recursing with the possible squares left and the current path
# when the length of the path is equal to n
# add the path to the valid path
#
