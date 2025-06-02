var sumOfLeftLeaves = function (root) {
  let sumLeft = 0;
  const DFS = (root) => {
    if (!root) return;
    if (root.left && !root.left.left && !root.left.right) {
      sumLeft += root.left.val;
    }
    DFS(root.left);
    DFS(root.right);
  };
  DFS(root);
  return sumLeft;
};

// Algo
// Use DFS
// If there is a left child and left child is a leaf add it to the total
