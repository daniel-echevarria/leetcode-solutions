class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def next_idx(idx):
            return (idx + nums[idx]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow = fast = i

            while True:
                slow = next_idx(slow)
                fast = next_idx(next_idx(fast))

                if (
                    slow == next_idx(slow)
                    or (nums[fast] > 0) != direction
                    or (nums[next_idx(fast)] > 0) != direction
                ):
                    break

                if slow == fast:
                    return True

            curr = i
            while nums[curr] != 0 and (nums[curr] > 0) == direction:
                next_step = next_idx(curr)
                nums[curr] = 0
                curr = next_step
        return False


nums = [-1, 2, 1, 2]
s = Solution()
print(s.circularArrayLoop(nums))
