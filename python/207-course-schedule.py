class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = {}
        for a, b in prerequisites:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]
        visited = set

    def dfs(node, graph, visited):
        if node not in graph or len(graph[node]) == 0:
            return True
        if node in visited:
            return False
        visited.add(node)
        for musts in graph[node]:
            dfs(node, graph, visited)




# Iterates through requisites and make a graph of each prerequisites for each course
# then DFS each course looking for loops
# if a loop is found return false

# if no loop is found return true
