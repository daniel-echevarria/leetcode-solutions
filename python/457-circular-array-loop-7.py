class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def next_step(i, forward):
            if (nums[i] > 0) != forward:
                return -1

            j = (i + nums[i]) % n
            return -1 if j == i else j

        for i in range(n):
            if nums[i] == 0:
                continue

            forward = nums[i] > 0
            slow = fast = i

            while True:
                slow = next_step(slow, forward)
                fast = next_step(fast, forward)

                if slow == -1 or fast == -1:
                    break

                fast = next_step(fast, forward)

                if fast == -1:
                    break

                if fast == slow:
                    return True
            curr = i
            while nums[curr] != 0:
                nxt = next_step(curr, forward)
                if nxt == -1:
                    break

                nums[curr] = 0
                curr = nxt

        return False
