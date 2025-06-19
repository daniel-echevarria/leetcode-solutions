var kthSmallest = function (root, k) {
  let count = 0;
  let solution = null;
  const DFS = (node) => {
    if (solution !== null) return;
    if (!node) return;

    DFS(node.left);
    count += 1;
    if (count === k) {
      solution = node.val;
      return;
    }
    DFS(node.right);
  };
  DFS(root);
  return solution;
};
