class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = {}
        for e in edges:
            graph[e] = (graph[e] or 0) + 1

        for keys in graph:

