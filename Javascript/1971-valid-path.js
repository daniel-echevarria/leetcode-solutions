// var validPath = function (n, edges, source, destination) {
//   if (source == destination) return true;
//   const graph = {};
//   for (const edge of edges) {
//     u = edge[0];
//     v = edge[1];
//     if (u == source && v == destination && v == source && u == destination)
//       return true;
//     graph[u] ? graph[u].push(v) : (graph[u] = [v]);
//     graph[v] ? graph[v].push(u) : (graph[v] = [u]);
//   }
//   let pathExists = false;
//   const visited = new Set();
//   const DFS = (node) => {
//     if (pathExists || visited.has(node)) return;
//     visited.add(node);
//     const connections = graph[node];
//     if (connections.includes(destination)) pathExists = true;
//     connections.forEach((el) => DFS(el));
//   };
//   DFS(source);
//   return pathExists;
// };

var validPath = function (n, edges, source, destination) {
  if (source == destination) return true;
  const graph = {};
  for (const edge of edges) {
    u = edge[0];
    v = edge[1];
    if ((u == source && v == destination) || (v == source && u == destination))
      return true;
    graph[u] ? graph[u].push(v) : (graph[u] = [v]);
    graph[v] ? graph[v].push(u) : (graph[v] = [u]);
  }
  let pathExists = false;
  const visited = new Set();
  const DFS = (node) => {
    if (pathExists || visited.has(node)) return;
    visited.add(node);
    const connections = graph[node];
    if (connections.includes(destination)) pathExists = true;
    connections.forEach((el) => DFS(el));
  };
  DFS(source);
  return pathExists;
};
