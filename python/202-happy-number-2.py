class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(val):
            return sum(int(i) ** 2 for i in str(val))

        slow = fast = n

        while True:
            slow = next_num(slow)
            fast = next_num(next_num(fast))

            if slow == 1 or fast == 1:
                return True

            if slow == fast:
                return False
