class Solution:
    def binaryGap(self, n: int) -> int:
        max_interval = 0
        bin_num = bin(n)[2:]
        previous_one = None
        for i, n in enumerate(bin_num):
            print(n)
            if n == "0":
                continue
            if previous_one != None:
                current_interval = i - previous_one
                max_interval = max(max_interval, current_interval)
            previous_one = i
        return max_interval


s = Solution()
# n = 22
n = 5
print(s.binaryGap(n))

# Algo
# get the binary number equivalent
# iterate through the binary rep
# keeping track of the longest interval
