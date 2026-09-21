class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def next_idx(curr):
            return (curr + nums[curr]) % n

        def is_moving_forward(idx):
            return nums[idx] > 0

        for i in range(n):
            forward = is_moving_forward(i)
            slow = fast = i
            while True:
                slow = next_idx(slow)
                fast = next_idx(next_idx(fast))
                if (
                    slow == next_idx(slow)
                    or is_moving_forward(fast) != forward
                    or is_moving_forward(next_idx(fast)) != forward
                ):
                    break

                if slow == fast:
                    return True

            curr = i
            while nums[curr] != 0 and is_moving_forward(curr) == forward:
                next_step = next_idx(curr)
                nums[curr] = 0
                curr = next_step

        return False


nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, -5]
s = Solution()
print(s.circularArrayLoop(nums))
