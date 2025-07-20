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


def dfs2(node, must_take, order, visited=set()):
    if node in visited:
        return
    visited.add(node)
    neighbors = must_take[node]
    if all(neighbor in order for neighbor in neighbors) or len(must_take[node]) == 0:
        order.append(node)
        return
    for neighbor in must_take[node]:
        dfs2(neighbor, must_take, order)


def dfs(node, must_take, must_be_taken, order):
    if not node in order:
        order.append(node)
    dependents = must_be_taken[node]
    for course in dependents:
        dfs2(course, must_take, order)


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        must_take = createMustTakeGraph(prerequisites)
        must_be_taken = createMustBeTakenGraph(prerequisites)
        starts = [course for course in range(numCourses) if len(must_take[course]) == 0]
        order = []
        for start in starts:
            dfs(start, must_take, must_be_taken, order)
        return order


s = Solution()
numCourses = 4
pres = [[1, 0], [2, 0], [3, 1], [3, 2]]

s.findOrder(numCourses, pres)


# Create a graph of the mustTake and mustBeTakenBy
# make an array of all the starting points (their must_take is empty)
# Launch a BFS on each of the starting points as such:
# push the current node the the order list unless it's already there
# if there is no neighbors return
# otherwise for each neighbor, check what courses they must take,
# If these courses are already in order, push the neighbor to order and continue
# otherwise call dfs on each neighbor, if there is a loop exit and return an empty array
# if order is as long as numCourses return order
