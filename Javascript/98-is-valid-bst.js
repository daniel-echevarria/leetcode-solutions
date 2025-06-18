const isValidBST = (root) => {
  let previousVal = null;
  let valid = true;
  const DFS = (node) => {
    if (!node || !valid) return;
    DFS(node.left);
    if (previousVal !== null && node.val <= previousVal) valid = false;
    previousVal = node.val;
    DFS(node.right);
  };
  DFS(root);
  return valid;
};
