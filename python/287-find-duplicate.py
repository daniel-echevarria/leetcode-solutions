class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            counts = nums.count(i)
            if counts > 1:
                return i
