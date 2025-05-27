var minDepth = function (root) {
  if (!root) return 0;
  let minDepth = Infinity;
  const BFS = (root, currentDepth = 1) => {
    if (!root) return;
    if (currentDepth > minDepth) return;
    if (!root.left && !root.right) {
      minDepth = Math.min(minDepth, currentDepth);
      return;
    }
    currentDepth++;
    BFS(root.left, currentDepth);
    BFS(root.right, currentDepth);
  };
  BFS(root);
  return minDepth;
};

// Algo
// At each stage recursively get the smallest depth from left and right
// return the smallest of the two values
