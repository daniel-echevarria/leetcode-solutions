class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        largest = 0
        stack = []

        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                largest = max(largest, width * height)
            stack.append(i)
        return largest


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
