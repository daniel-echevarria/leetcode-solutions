from collections import deque


class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        n = len(adj)
        queue = deque([0])
        res = []
        visited = [False] * n
        while queue:
            node = queue.popleft()
            if visited[node]:
                continue
            res.append(node)
            visited[node] = True
            for neighbor in adj[node]:
                queue.append(neighbor)
        print(res)
        return res


s = Solution()
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
s.bfs(adj)
