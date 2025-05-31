var searchBST = function (root, val) {
  let result = null;
  const DFS = (root) => {
    if (!root) return;
    if (root.val === val) {
      result = root;
      return;
    }
    val > root.val ? DFS(root.right) : DFS(root.left);
  };
  DFS(root);
  return result;
};
