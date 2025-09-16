from collections import defaultdict


class Solution:

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        state = [0] * numCourses  # 0: unvisited, 1: visiting, 2: done
        result = []
        has_cycle = False

        def dfs(node):
            nonlocal has_cycle
            if has_cycle:
                return
            state[node] = 1
            for child in graph[node]:
                if state[child] == 1:
                    has_cycle = True
                    return
                if state[child] == 2:
                    continue
                dfs(child)
            state[node] = 2
            result.append(node)

        for i in range(numCourses):
            if state[i] == 2:
                continue
            dfs(i)

        answer = [] if has_cycle else result
        return answer


# ex1 = [[1, 0], [2, 0], [3, 1], [3, 2]]
# # 4
# ex2 = [[0, 1], [1, 0]]
# # 2


# s = Solution()
# s.findOrder(4, ex1)
# s.findOrder(2, ex2)
