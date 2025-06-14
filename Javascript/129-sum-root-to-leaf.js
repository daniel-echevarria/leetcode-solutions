var sumNumbers = function (root) {
  let total = 0;
  const DFS = (node, string = "") => {
    if (!node) return;
    if (!node.left && !node.right) {
      total += +(string + node.val);
      return;
    }
    DFS(node.left, string + node.val);
    DFS(node.right, string + node.val);
  };
  DFS(root);
  return total;
};
