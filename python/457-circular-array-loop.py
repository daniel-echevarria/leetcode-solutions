class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        for i, jump in enumerate(nums):
            direction = -1 if nums[i] < 0 else 1
            prev = None
            fast = slow = i
            while True:
                if (
                    nums[slow] < 0
                    and direction == 1
                    or nums[slow] > 0
                    and direction == -1
                    or slow == prev
                ):
                    break
                prev = slow
                slow = slow + nums[slow]
                if slow > len(nums):
                    slow = slow - len(nums)
                fast = nums[fast] + nums[nums[fast]]
                if fast > len(nums):
                    fast = fast - len(nums)
                if fast == slow:
                    return True
        return False


nums = [2, -1, 1, 2, 2]
s = Solution()
print(s.circularArrayLoop(nums))
