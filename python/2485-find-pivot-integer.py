class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = []
        for i in range(1, n + 1):
            arr.append(i)

        total = sum(arr)
        curr = 0
        for i in range(n + 1):
            curr += i
            if curr == total - curr + i:
                return i
        return -1


s = Solution()
print(s.pivotInteger(1))

# Create the array
# get the total sum
# iterate while keeping the sum
# if at some point the sum is the same as the total minus the sum + the current
# return the index
# after iteration
# return the -1
