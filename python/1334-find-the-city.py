from collections import defaultdict


def get_max_cities(graph, node, threshold):
    visited = set()
    ultimate = set()
    original = node

    def dfs(graph, node, threshold):
        if threshold < 0 or node == original:
            return
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor[0] in visited:
                continue
            b, w = neighbor
            dfs(graph, b, threshold - w)

    for neighbor in graph[node]:
        b, w = neighbor
        dfs(graph, b, threshold - w)
        ultimate.update(visited)
        visited = set()
    return len(ultimate)


def generate_graph(edges, distanceThreshold):
    graph = defaultdict(list)
    for e in edges:
        a, b, w = e
        if w <= distanceThreshold:
            graph[a].append((b, w))
            graph[b].append((a, w))
    return graph


class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:
        graph = generate_graph(edges, distanceThreshold)
        num_cities_graph = {}
        for i in range(n):
            num_cities_graph[i] = get_max_cities(graph, i, distanceThreshold)
        most_isolated_city = (-1, n)
        print(num_cities_graph)
        for i in range(n):
            connections = num_cities_graph[i]
            if connections <= most_isolated_city[1]:
                most_isolated_city = (i, connections)
        return most_isolated_city[0]


s = Solution()
n = 6
edges = [[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]]
threshold = 20
s.findTheCity(n, edges, threshold)


# Make a graph of the connected cities with their weight
# Add it to the graph only if the weight is equal or smaller to the distanceThreshold!
# Iterate through each city and see how many cities it can reach
# Return the city with the smallest number of cities but bigger number itself
