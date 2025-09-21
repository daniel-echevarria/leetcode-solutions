from collections import defaultdict


class Solution:

    def generate_graph(self, edges):
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        return graph

    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n < 2:
            return [0]

        graph = self.generate_graph(edges)
        leaves = [leaf for leaf in graph if len(graph[leaf]) == 1]
        while n > 2:
            new_leaves = []
            for leaf in leaves:
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor]) == 1:
                        new_leaves.append(neighbor)
                del graph[leaf]
            leaves = new_leaves
            n = len(graph)
        return list(graph.keys())


s = Solution()
s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
