class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)

        return res


s = Solution()
temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(s.dailyTemperatures(temps))

# Algo
# Declare a res array filled with 0 for each temperature
# Declare an empty stack
# Iterate backwards through the temperatures
# for each iteration
# declare a count with initial value of 0
# launch a loop that pops from the stack as long as the value is equal or smaller
# each time adding one to the count
# after the loop the result at that index gets the count
# push the temperature to the stack
# after iteration return the result
