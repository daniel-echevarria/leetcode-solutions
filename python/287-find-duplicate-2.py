class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def next_number(n):
            return nums[n]

        slow, fast = next_number(0), next_number(next_number(0))

        while slow != fast:
            slow = next_number(slow)
            fast = next_number(next_number(fast))

        finder = 0

        while slow != finder:
            slow = next_number(slow)
            finder = next_number(finder)

        return slow
