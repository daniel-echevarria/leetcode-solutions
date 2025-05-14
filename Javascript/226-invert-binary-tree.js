var invertTree = function (root) {
  if (!root) {
    return null;
  }

  [root.left, root.right] = [root.right, root.left];
  invertTree(root.left);
  invertTree(root.right);
  return root;
};

// Algo invertTree
// Given the root of a binary tree
// root left gets root right and vice versa
// recursively
