var isBalanced = function (root) {
  let isBalanced = true;
  const DFS = (root) => {
    if (!root) return 0;
    const left = 1 + DFS(root.left);
    const right = 1 + DFS(root.right);
    if (Math.abs(left - right) > 1) isBalanced = false;
    const maxHeight = Math.max(left, right);
    return maxHeight;
  };
  DFS(root);
  return isBalanced;
};

// Algo
// Traverse the tree DFS checking the height of the left and right children
// If at any stage the absolute difference is bigger than 1 return false
