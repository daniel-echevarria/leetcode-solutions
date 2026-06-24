class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            counts = nums.count(i)
            if counts > 1:
                return i


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        fast = slow = 0
        n = len(nums)
        nodes_visited = 0

        while nodes_visited < n:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if nums[slow] == nums[fast]:
                return nums[slow]
            nodes_visited += 1

        return False
