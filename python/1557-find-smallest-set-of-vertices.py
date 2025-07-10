class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        reachable = set(to for _, to in edges)
        return [ver for ver in range(n) if ver not in reachable]


s = Solution()
s.findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]])


# Create an array from 0 to n -1
# Iterate through the edges and remove from the list all the reachable vertices (to)
# return the vertices

# Declare a map reached_by
# Iterate through the edges list and add or create
# to : [from]
