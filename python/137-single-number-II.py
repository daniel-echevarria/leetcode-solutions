class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        print("cool")


n = 13
counts = 0

while n:
    n = n & n - 1
    counts += 1

print(counts)
