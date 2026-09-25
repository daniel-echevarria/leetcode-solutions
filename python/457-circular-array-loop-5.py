class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def next_move(i, forward):
            if (nums[i] > 0) != forward:
                return -1

            j = (i + nums[i]) % n
            return -1 if j == i else j

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = fast = i
            forward = nums[i] > 0

            while True:
                slow = next_move(slow, forward)
                fast = next_move(fast, forward)

                if slow == -1 or fast == -1:
                    break

                fast = next_move(fast, forward)

                if fast == -1:
                    break

                if fast == slow:
                    return True

            curr = i
            while nums[curr] != 0:
                next_idx = next_move(curr, forward)
                if next_idx == -1:
                    break
                nums[curr] = 0
                curr = next_idx
        return False
