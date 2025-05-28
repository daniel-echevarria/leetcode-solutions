var preorderTraversal = function (root) {
  const preOrder = [];
  const DFS = (root) => {
    if (!root) return;
    preOrder.push(root.val);
    DFS(root.left);
    DFS(root.right);
  };
  DFS(root);
  return preOrder;
};

// Declare an array preorder
// Traverse the Array DFS style
// push the root value
// call DFS on the left node
// call DFS on the right node
// return preorder
