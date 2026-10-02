class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def next_step(i, forward):
            if (nums[i] > 0) != forward:
                return -1

            j = (nums[i] + i) % n

            if j == i:
                return -1

            return j

        for i in range(n):
            slow = fast = i
            forward = nums[i] > 0

            while True:
                slow = next_step(slow, forward)
                fast = next_step(fast, forward)

                if slow == -1 or fast == -1:
                    break

                fast = next_step(fast, forward)

                if fast == -1:
                    break

                if slow == fast:
                    return True
            curr = i
            while nums[curr] != 0 and next_step(curr, forward) != -1:
                nxt = next_step(curr, forward)
                nums[curr] = 0
                curr = nxt
        return False


nums = [-2, 1, -1, -2, -2]
s = Solution()
print(s.circularArrayLoop(nums))
