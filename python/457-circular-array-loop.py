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


class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        def move_next(idx):
            return (nums[idx] + idx) % len(nums)

        def same_direction(i, moving_forward):
            return nums[i] > 0 == moving_forward

        for i, n in enumerate(nums):
            fast = slow = i
            moving_forward = nums[i] > 0
            while True:
                prev = slow
                slow = move_next(slow)
                fast = move_next(move_next(fast))

                if (
                    nums[slow] > 0
                    and not moving_forward
                    or nums[slow] < 0
                    and moving_forward
                    or prev == slow
                ):
                    break

                if slow == fast:
                    return True
        return False


class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            slow = fast = i
            direction = nums[i] > 0

            while (
                (nums[slow] > 0) == direction
                and (nums[fast] > 0) == direction
                and (nums[next_index(fast)] > 0) == direction
            ):
                slow = next_index(slow)
                fast = next_index(next_index(fast))

                if fast == slow:
                    if next_index(slow) == slow:
                        break
                    return True
        return False


nums = [1, -1, 5, 1, 4]
s = Solution()
print(s.circularArrayLoop(nums))
