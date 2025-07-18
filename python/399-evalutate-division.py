def create_ratios_graph(equations, values):
    graph = {}
    for i in range(len(equations)):
        a, b = equations[i]
        if graph.get(a):
            graph[a].append((b, values[i]))
        else:
            graph[a] = [(b, values[i])]
        if graph.get(b):
            graph[b].append((a, 1 / values[i]))
        else:
            graph[b] = [(a, 1 / values[i])]
    return graph


def dfs(node, goal, graph, visited, ratio=1):
    if not graph.get(node) or not graph.get(goal):
        return
    if node in visited:
        return
    neighbors = graph.get(node)
    visited.add(node)
    if node == goal:
        return ratio
    for neighbor in neighbors:
        result = dfs(neighbor[0], goal, graph, visited, ratio * neighbor[1])
        if not result:
            continue
        return result


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        graph = create_ratios_graph(equations, values)
        results = []
        visited = set()
        for query in queries:
            start, goal = query
            results.append(dfs(start, goal, graph, visited) or -1)
            visited.clear()
        return results


# Algo
# Create graph of the ratios
# Then for each query, dfs in the graph from a to b
# while multiplying the weights
# if not possible to find the ratio
# return - 1
# if a and b are the same, return 1


equ = [["a", "b"], ["c", "d"]]
vals = [1.0, 1.0]
queries = [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]

s = Solution()
s.calcEquation(equ, vals, queries)
