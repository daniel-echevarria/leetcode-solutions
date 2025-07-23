from collections import defaultdict


def get_max_cities(graph, node, threshold):
    max_cities = 0

    def dfs(graph, node, threshold):
        if threshold <= 0:
            return
        max_cities += 1
        for neighbor in graph[node]:
            b, w = neighbor
            dfs(b, threshold - w)

    dfs(graph, node, threshold)
    return max_cities


class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:
        graph = defaultdict(list)
        for e in edges:
            a, b, w = e
            if w <= distanceThreshold:
                graph[a].append((b, w))
                graph[b].append((a, w))
        num_cities_graph = {}
        for i in range(n):
            num_cities_graph[i] = get_max_cities(graph, i, threshold)
        print(num_cities_graph)


s = Solution()
n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
threshold = 4
s.findTheCity(n, edges, threshold)


# Make a graph of the connected cities with their weight
# Add it to the graph only if the weight is equal or smaller to the distanceThreshold!
# Iterate through each city and see how many cities it can reach
# Return the city with the smallest number of cities but bigger number itself
