var maxDepth = function (root) {
  let maxSoFar = 0;
  const DFS = (root, currentDepth = 0) => {
    if (!root) return;
    if (root.children.length === 0) {
      maxSoFar = Math.max(maxSoFar, currentDepth + 1);
      return;
    }

    root.children.forEach((child) => {
      DFS(child, currentDepth + 1);
    });
  };
  DFS(root);
  return maxSoFar;
};
