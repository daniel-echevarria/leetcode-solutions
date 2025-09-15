from collections import defaultdict


def createGraph(prerequisites):
    graph = defaultdict(list)
    for v in prerequisites:
        a, b = v
        graph[a].append(b)
    return graph


class Solution:

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        explored = defaultdict(str)
        result = []
        graph = createGraph(prerequisites)
        has_cycle = False

        def dfs(node):
            nonlocal has_cycle
            explored[node] = "visiting"
            for child in graph[node]:
                if explored[child] == "visiting":
                    has_cycle = True
                    return
                if explored[child] == "done":
                    continue
                dfs(child)
            explored[node] = "done"
            result.append(node)

        for i in range(numCourses):
            if explored[i] == "done":
                continue
            dfs(i)

        answer = [] if has_cycle else result
        return answer


# ex1 = [[1, 0], [2, 0], [3, 1], [3, 2]]
# # 4
# ex2 = [[0, 1], [1, 0]]
# # 2


# s = Solution()
# s.findOrder(2, ex2)
