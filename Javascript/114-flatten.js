var flatten = function (root) {
  const preOrder = [];
  const DFS = (node) => {
    if (!node) return;
    preOrder.push(node.val);
    DFS(node.left);
    DFS(node.right);
  };
  DFS(root);
  let dummy = new TreeNode(0);
  let currentNode = new TreeNode(preOrder.shift());
  dummy.right = currentNode;
  while (preOrder.length) {
    currentNode.right = new TreeNode(preOrder.shift());
    currentNode = currentNode.right;
  }
  root = dummy.right;
  return root;
};
