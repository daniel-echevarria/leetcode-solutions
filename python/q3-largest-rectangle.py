class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        stack = []
        next_smaller = [0] * n
        previous_smaller = [0] * n
        res = [0] * n

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            next_smaller[i] = stack[-1] if stack else n
            stack.append(i)

        stack = []
        for j in range(n):
            while stack and heights[stack[-1]] >= heights[j]:
                stack.pop()
            previous_smaller[j] = stack[-1] if stack else -1
            stack.append(j)

        for k in range(n):
            start = previous_smaller[k] + 1
            end = next_smaller[k]
            width = end - start
            res[k] = heights[k] * width

        return max(res)


s = Solution()
heights = [2, 1, 5, 6, 2, 3]
heights = [5, 4, 1, 2]
print(s.largestRectangleArea(heights))


# Algo
# Declare an empty stack
# Declare a next smaller array with initial values being -1
# Iterate backwards
# while the stack is not empty and the top value is bigger equal to the current vale
# pop the stack
# after that if the stack is not empty
# That is the index of the next smaller
# update the next smaller value in the array
# then iterate through the array
# and multiply by the distance to the next smaller in a result array
