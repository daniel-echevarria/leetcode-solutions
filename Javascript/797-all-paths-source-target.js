var allPathsSourceTarget = function (graph) {
  const n = graph.length;
  const allPaths = [];
  const DFS = (node, path = []) => {
    path.push(node);
    if (path.includes(n - 1)) {
      allPaths.push(path);
      return;
    }
    if (graph[node].length < 1) return;
    for (const link of graph[node]) {
      DFS(link, [...path]);
    }
  };
  DFS(0);
  return allPaths;
};

// Declare an empty array allPaths
// Traverse the graph BFS style while keeping track of the visited nodes
// If there is no node you can visit from the current node, push the path to the allPaths
// After traversal return allPaths
