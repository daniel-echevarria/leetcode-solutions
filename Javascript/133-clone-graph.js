var cloneGraph = function (node) {
  if (!node) return;

  const visited = new Map();
  const DFS = (current) => {
    if (visited.has(current)) return visited.get(current);

    const clone = new _Node(current.val);
    visited.set(current, clone);
    for (const neighbor of current.neighbors) {
      clone.neighbors.push(DFS(neighbor));
    }

    return clone;
  };

  return DFS(node);
};
