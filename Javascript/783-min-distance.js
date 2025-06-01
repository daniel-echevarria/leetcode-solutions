var minDiffInBST = function (root) {
  const inorder = [];
  const DFS = (root) => {
    if (!root) return;

    DFS(root.left);
    inorder.push(root.val);
    DFS(root.right);
  };
  DFS(root);

  let minDistance = 100000;
  for (let i = 1; i < inorder.length; i++) {
    const distance = inorder[i] - inorder[i - 1];
    minDistance = Math.min(minDistance, distance);
  }

  return minDistance;
};

// traverse the tree inorder storing the values
// iterate through the array comparing the distance
