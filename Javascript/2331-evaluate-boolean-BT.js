var evaluateTree = function (root) {
  if (!root.left) return root.val === 1;
  const left = evaluateTree(root.left);
  const right = evaluateTree(root.right);
  return root.val === 2 ? left || right : left && right;
};

// use DFS
// Get the value of the left child
// Get the value of the right child
// return the result of the operation left, current, right
// return end result
