var binaryTreePaths = function (root) {
  const paths = [];
  const DFS = (root, path = "") => {
    if (!root) return;
    if (!root.left && !root.right) {
      paths.push(path + root.val);
      return;
    }
    DFS(root.left, path + root.val + "->");
    DFS(root.right, path + root.val + "->");
  };
  DFS(root);
  return paths;
};
