class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def next_valid(i, forward):
            if (nums[i] > 0) != forward:
                return -1

            j = (i + nums[i]) % n
            return -1 if j == i else j

        for i in range(n):
            forward = nums[i] > 0
            slow = fast = i

            while True:
                slow = next_valid(slow, forward)
                fast = next_valid(fast, forward)

                if fast == -1 or slow == -1:
                    break

                fast = next_valid(fast, forward)

                if fast == -1:
                    break

                if fast == slow:
                    return True

            curr = i
            while nums[curr] != 0:
                nxt = next_valid(curr, forward)
                if nxt == -1:
                    break
                nums[curr] = 0
                curr = nxt
        return False
