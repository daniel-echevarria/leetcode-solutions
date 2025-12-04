class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        operations = []
        stack = []

        for i in range(1, n + 1):
            stack.append(i)
            operations.append("Push")
            if stack == target[: len(stack)]:
                if len(stack) == len(target):
                    return operations
                continue
            stack.pop()
            operations.append("Pop")
        return operations


# Algo
# Iterate in the range of n
# push it to the stack
# if the stack doesn't match with the target up to that point
# pop the stack
# if the stack match the target and the length of the stack is the same of the target
# return the operations

# target = [1, 3, 6]
# n = 8
target = [2, 3, 4]
n = 4

s = Solution()
print(s.buildArray(target, n))
