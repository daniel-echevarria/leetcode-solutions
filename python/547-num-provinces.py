def createGraph(isConnected):
    n = len(isConnected)
    connected_cities = {}
    for i in range(n):
        for j in range(n):
            if isConnected[i][j] == 0 or i == j:
                continue
            if i in connected_cities:
                connected_cities[i].add(j)
            else:
                connected_cities[i] = set([j])
    return connected_cities

def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)
    linkedCities = graph.get(node)
    if not linkedCities:
        return
    for link in linkedCities:
        dfs(link, graph, visited)


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        connections = createGraph(isConnected)
        provinces_count = 0
        visited = set()
        for city in range(n):
            if city in visited:
                continue
            provinces_count +=1
            dfs(city, connections, visited)
        return(provinces_count)

s = Solution()
s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])









#  Declare a variable n that gets isConnected length
#  Iterate through isConnected and make a graph of the connected cities as such:
#  if i,j == 1
#  then check if i exits and add j or create i: j
#  do the same for j, check if j exits, add i if yes or create
#  if i,j == 0 continue
#  this gives is a graph of the adjacency list

#  Declare a visited set
#  Then we iterate from 0 to n - 1
#  if the city  is in the visited set or not in the graph we continue
#  If we find the city in the graph we
#  add 1 to the provinces and launch dfs
#  the dfs goes until all the neighbors are visited
#  it returns if the node is visited
#  otherwise it adds the node anc calls dfs in all the neighbors

#  finally return numProvinces
