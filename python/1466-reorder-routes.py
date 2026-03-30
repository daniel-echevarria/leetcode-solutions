from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)

        visited = set()
        total_edges = 0
        round_edges = 0

        def dfs(city):
            nonlocal round_edges
            nonlocal total_edges
            for neighbor in adj[city]:
                if neighbor == 0:
                    round_edges = 0
                    continue
                if neighbor not in visited:
                    visited.add(neighbor)
                    round_edges += 1
                    dfs(neighbor)
                total_edges += round_edges
                round_edges = 0

        for i in range(n - 1):
            if i not in visited:
                dfs(i)
                visited.add(i)

        return total_edges


# Build an agency list
# initialize an edge count to 0
# then traverse the graph from 0 keeping track of visited cities
# for each connected city add edges (change sides) until they are no more or that the city is in visited
# every time you move to a new city add one to edges and add it to visited
# then iterate on the remaining keys doing the same


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append((b, 1))
            adj[b].append((a, 0))

        visited = set()

        def dfs(city):
            changes = 0
            visited.add(city)
            for neighbor, cost in adj[city]:
                if neighbor not in visited:
                    changes += cost
                    changes += dfs(neighbor)
            return changes

        return dfs(0)


con = [[0, 2], [0, 3], [4, 1], [4, 5], [5, 0]]
n = 6
# con = [[1, 2], [2, 0]]
# n = 3
# con = [[0, 6], [6, 3], [1, 3], [2, 1], [4, 0], [4, 5]]
# n = 7
s = Solution()
print(s.minReorder(n, con))
