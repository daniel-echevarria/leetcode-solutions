from collections import defaultdict


def create_graph(prerequisites):
    graph = defaultdict(list)
    for pre in prerequisites:
        a, b = pre
        graph[a].append(b)
    return graph


def dfs(course, visited, graph, fine):
    if len(graph[course]) == 0 or course in fine:
        return False
    if course in visited:
        return True
    visited.add(course)
    for neighbor in graph[course]:
        loop_exits = dfs(neighbor, visited, graph, fine)
        if loop_exits:
            return True
        fine.add(neighbor)
    return False


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = create_graph(prerequisites)
        fine = set()
        for course in range(numCourses):
            visited = set()
            loop_exits = dfs(course, visited, graph, fine)
            if loop_exits:
                return False
            fine.add(course)
        return True


s = Solution()
num = 8
pre = [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]

s.canFinish(num, pre)

# Algo
# First build a graph of the mustTake for each course
# Then iterate from 0 and see if there is any loop
# If there is a loop return false
# Otherwise return true
