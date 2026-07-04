class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            counts = nums.count(i)
            if counts > 1:
                return i


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        fast = slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0

        while fast != slow2:
            fast = nums[fast]
            slow2 = nums[slow2]

        return slow2


nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
# nums = [3, 1, 3, 4, 2]

s = Solution()
print(s.findDuplicate(nums))
