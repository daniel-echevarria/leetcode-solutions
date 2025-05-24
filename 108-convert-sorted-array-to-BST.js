var sortedArrayToBST = function (nums) {
  const placedNode = (val, root = null) => {
    if (!root) return new TreeNode(val);
    if (val < root.val) root.left = placedNode(val, root.left);
    if (val > root.val) root.right = placedNode(val, root.right);
  };

  for (let num in nums) {
    placedNode(num);
  }
  return root;
};

// Algo
// Find the middle of the array
// That becomes the root node
// iterate through the array placing the nodes
// Algo placeNode
// if the current root is null create a node with the value
// if the current root value is bigger
// call placeNode on the left child
// if the root value is smaller
// placedNode on the right child
