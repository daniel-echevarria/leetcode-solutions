class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def valid_move(i, forward):
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
                slow = valid_move(slow, forward)
                fast = valid_move(fast, forward)

                if slow == -1 or fast == -1:
                    break

                fast = valid_move(fast, forward)

                if fast == -1:
                    break

                if slow == fast:
                    return True

            curr = i
            while nums[curr] != 0:
                idx = valid_move(curr, forward)

                if idx == -1:
                    break

                nums[curr] = 0
                curr = idx
        return False
