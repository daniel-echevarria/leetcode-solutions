class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        left = []
        right = []
        for a in asteroids:
            if a > 0:
                right.append(a)
                continue
            while right and right[-1] < abs(a):
                right.pop()
            if not right:
                left.append(a)
                continue
            if right[-1] > abs(a):
                continue
            if right[-1] == abs(a):
                right.pop()
        return left + right


a = [3, 5, -6, 2, -1, 4]
s = Solution()
print(s.asteroidCollision(a))


# Algo
# iterate through the asteroids
# pushing them to a stack
# the moment an asteroid is going left (negative)
# pop from the stack until the front of the stack is bigger than the absolute value of asteroid
# of the stack is empty
# then 3 things can happen, if the asteroid is smaller, just continue
# if the stack is empty, push the asteroid
# if the asteroid is the same size, pop and continue
# return the result
