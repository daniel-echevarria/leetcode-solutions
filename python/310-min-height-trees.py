from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


class Solution:
    def generate_graph(self, edges):
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        return graph

    def buildTree(self, rootVal, graph, n):
        visited = [False] * n
        root = TreeNode(rootVal)
        queue = deque([root])
        height = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if visited[node.val]:
                    continue
                visited[node.val] = True
                for neighbor in graph[node.val]:
                    if visited[neighbor]:
                        continue
                    child = TreeNode(neighbor)
                    node.children.append(child)
                    queue.append(child)
            height += 1
        return (root, height - 1)

    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        mhts = []
        graph = self.generate_graph(edges)
        print(graph)
        min_height = n
        for i in range(n):
            root, height = self.buildTree(i, graph, n)
            if height > min_height:
                continue
            if height == min_height:
                mhts.append(root.val)
            if height < min_height:
                min_height = height
                mhts = [root.val]
        return mhts

        first_tree = self.buildTree(0, graph, n)


s = Solution()
s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
