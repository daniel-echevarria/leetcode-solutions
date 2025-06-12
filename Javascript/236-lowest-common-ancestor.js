var lowestCommonAncestor = function (root, p, q) {
  const DFS = (node, goal, path = []) => {
    if (path.includes(goal)) return path;
    if (!node) return;
    path.push(node);
    if (node === goal) return path;
    const left = DFS(node.left, goal, path);
    const right = DFS(node.right, goal, path);
    return left || right;
  };
  const qPath = DFS(root, q);
  const pPath = DFS(root, p);
  console.log(qPath, pPath);
};

// Find p in the tree and keep track of the path
// if q exists in the path return q
// otherwise find q in the three and keep track of the path
// once both path are found
// Iterate through the path until they differ and return the last common path
