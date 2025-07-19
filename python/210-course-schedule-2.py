from collections import defaultdict


def createMustTakeGraph(prerequisites):
    graph = defaultdict(list)
    for pre in prerequisites:
        a, b = pre
        graph[a].append(b)
    return graph


def createMustBeTakenGraph(prerequisites):
    graph = defaultdict(list)
    for pre in prerequisites:
        a, b = pre
        graph[b].append(a)
    return graph


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        must_take = createMustTakeGraph(prerequisites)
        must_be_taken = createMustBeTakenGraph(prerequisites)
        starts = [course for course in range(numCourses) if len(must_take[course]) == 0]
        print(starts)


s = Solution()
numCourses = 2
pres = [[1, 0]]
s.findOrder(numCourses, pres)


# Create a graph of the mustTake and mustBeTakenBy
# Find one course that mustTake nothing
# Launch a dfs on that course for the mustBeTakenBy while pushing into order
# delete that starting point from the graph
# do the same for the next mustTake nothing
# if order is as long as numCourses return order
# if there is no more mustTake nothing return empty array
