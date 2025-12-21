class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        removed = 0
        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row - 1][col] > strs[row][col]:
                    if col > 0:
                        if (
                            strs[row - 1][col - (1 + removed)]
                            == strs[row][col - (1 + removed)]
                        ):
                            removed += 1
                            break
        return removed


# st = ["cba", "daf", "ghi"]
st = ["zyx", "wvu", "tsr"]
# st = ["xga", "xfb", "yfa"]
s = Solution()
print(s.minDeletionSize(st))


# Algo
# make the grid
# compare each string to the sorted version
# count deltetion
