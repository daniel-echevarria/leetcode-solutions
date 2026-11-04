class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(v):
            return sum(int(x) ** 2 for x in str(v))

        slow = fast = n

        while True:
            slow = next_num(slow)
            fast = next_num(next_num(fast))

            if slow == 1:
                return True

            if slow == fast:
                return False
