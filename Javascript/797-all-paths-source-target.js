var allPathsSourceTarget = function (graph) {
  const allPaths = [];
  const path = [0];
  const DFS = (node) => {
    if (node == graph.length - 1) {
      allPaths.push([...path]);
      return;
    }
    for (const link of graph[node]) {
      path.push(link);
      DFS(link, path);
      path.pop();
    }
  };
  DFS(0);
  return allPaths;
};
