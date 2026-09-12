class Solution:
    def isHappy(self, n: int) -> bool:
        def next_number(n):
            return sum(int(d) ** 2 for d in str(n))

        slow = fast = n
        while True:
            slow = next_number(slow)
            fast = next_number(next_number(fast))

            if slow == fast:
                return slow == 1


n = 19
s = Solution()
print(s.isHappy(n))

# transform the number into a string, split it
# transform ins back to number, square them
# then add them back, if the result is 1 return true
# if there is a cycle return false
