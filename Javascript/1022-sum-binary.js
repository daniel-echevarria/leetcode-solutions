var sumRootToLeaf = function (root) {
  let total = 0;
  const DFS = (root, current = "") => {
    if (!root) return;
    current += root.val;
    if (!root.left && !root.right) total += parseInt(current, 2);
    DFS(root.left, current);
    DFS(root.right, current);
  };
  DFS(root);
  return total;
};

// Algo
// Declare a total variable
// Declare a currentBinary empty string
// Traverse the tree in preorder
// add the current value to the currentBinary
// When reaching a leaf push the currentBinary converted to a number converted to a base10
// after the traversal sum the all array
