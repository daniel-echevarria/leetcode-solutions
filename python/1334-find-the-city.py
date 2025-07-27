from collections import defaultdict
import math
import heapq


class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:

        def generate_graph():
            graph = defaultdict(list)
            for a, b, w in edges:
                graph[a].append((b, w))
                graph[b].append((a, w))
            return graph

        graph = generate_graph()

        def get_shortest_paths(source):
            distance_dict = defaultdict(lambda: math.inf)
            distance_dict[source] = 0
            h = [(0, source)]
            visited = set()
            while len(h):
                weight, city = heapq.heappop(h)
                if city in visited:
                    continue
                visited.add(city)
                for neighbor, edge_w in graph[city]:
                    if neighbor not in visited:
                        net_weight = weight + edge_w
                        if net_weight < distance_dict[neighbor]:
                            distance_dict[neighbor] = net_weight
                            heapq.heappush(h, (net_weight, neighbor))
            return distance_dict

        max_cities_graph = {}

        def is_reachable(pair):
            city, distance = pair
            return distance <= distanceThreshold

        for city in range(n):
            shortest_path_graph = get_shortest_paths(city)
            max_cities_graph[city] = len(
                dict(filter(is_reachable, shortest_path_graph.items()))
            )
        most_isolated = (0, math.inf)
        for city in max_cities_graph:
            if max_cities_graph[city] <= most_isolated[1]:
                most_isolated = (city, max_cities_graph[city])
        return most_isolated[0]


n = 5
edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
distanceThreshold = 2

s = Solution()
s.findTheCity(n, edges, distanceThreshold)

# Algo
# For each city make a graph of the shortest distance to each other city as such:
# Given a node the distance to itself is 0 and all others are inf
# Traverse the node using BFS while updating the shortestPath distance if found a shorter path,
# Then from that graph start a new graph of the number of reachable cities
# (cities where the shortest path is smaller or equal to the distanceThreshold)
# From that last graph return the mostIsolatedCity with the biggest index
