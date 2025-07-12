var canFinish = function (numCourses, prerequisites) {
  const graph = {};
  for (const pair of prerequisites) {
    const [a, b] = pair;
    graph[a] ? graph[a].push(b) : (graph[a] = [b]);
  }
  let visited = new Set();
  const dfs = (node) => {
    if (!graph[node]) return true;
    if (visited.has(node)) return false;
    visited.add(node);
    for (const pre of graph[node]) {
      if (dfs(pre)) continue;
      return false;
    }
  };
  let noLoop = true;
  for (let i = 0; i < numCourses; i++) {
    visited = new Set();
    if (dfs(i)) continue;
    noLoop = false;
  }
  return noLoop;
};

// Iterate through the courses in the graph and traverse them DFS
// if the course as no requisites return true
// if the course as a requisites that was already visited return false
// recursively call dfs on all the requisites
canFinish(2, [
  [2, 0],
  [1, 0],
  [3, 1],
  [3, 2],
  [1, 3],
]);
