class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix_sum = [None] * len(nums)
        self.nums = nums
        for i, n in enumerate(nums):
            if i == 0:
                self.prefix_sum[i] = n
                continue
            self.prefix_sum[i] = self.prefix_sum[i - 1] + n

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        return self.prefix_sum[right] - self.prefix_sum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
