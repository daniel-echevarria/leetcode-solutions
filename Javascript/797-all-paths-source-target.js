var allPathsSourceTarget = function (graph) {
  const allPaths = [];
  let path = [];
  const DFS = (node) => {
    path.push(node);
    if (graph[node].length < 1) {
      allPaths.push(path);
      path = [];
      return;
    }
    for (const link of graph[node]) {
      DFS(link);
    }
  };
  DFS(0);
  return allPaths;
};

// Declare an empty array allPaths
// Traverse the graph BFS style while keeping track of the visited nodes
// If there is no node you can visit from the current node, push the path to the allPaths
// After traversal return allPaths
