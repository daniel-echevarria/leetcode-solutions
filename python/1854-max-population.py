class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        logs = list(map(lambda x: [x[0] - 1950, x[1] - 1950], logs))
        population = [0] * 101

        for birth, death in logs:
            population[birth] += 1
            population[death] -= 1

        max_pop = cur = year = 0

        for i in range(101):
            cur += population[i]
            if cur > max_pop:
                max_pop = cur
                year = i

        return year + 1950


s = Solution()
# logs = [[1993, 1999], [2000, 2010]]
logs = [[1950, 1961], [1960, 1971], [1970, 1981]]
print(s.maximumPopulation(logs))

# make an array of 100 items
# iterate through the logs
# add 1 to the years matching the condition
# for example if the person lived from 1950 to 2000
# the element 0 to 49 get + 1
# find the max value,
# return the index of the max value
