var postorderTraversal = function (root) {
  const postOrder = [];
  const DFS = (root) => {
    if (!root) return;
    DFS(root.left);
    DFS(root.right);
    postOrder.push(root.val);
  };
  DFS(root);
  return postOrder;
};

// Declare a postOrder empty array
// Traverse the tree DFS
// First call on the left node
// then push the current node
// the call on the right node
