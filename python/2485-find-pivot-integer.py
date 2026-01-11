class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = []
        prefix = []
        curr = 0
        for i in range(1, n + 1):
            arr.append(i)
            prefix.append(curr + i)
            curr += i

        l, r = 0, n - 1


class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        x = int(total**0.5)
        return x if x * x == total else -1


s = Solution()
print(s.pivotInteger(8))

# Create the array
# get the total sum
# iterate while keeping the sum
# if at some point the sum is the same as the total minus the sum + the current
# return the index
# after iteration
# return the -1
