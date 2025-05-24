var sortedArrayToBST = function (nums) {
  const placedNode = (root, val) => {
    if (!root) return new TreeNode(val);
    if (val < root.val) root.left = placedNode(root.left, val);
    if (val > root.val) root.right = placedNode(root.right, val);
  };
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
