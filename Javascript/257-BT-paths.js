var binaryTreePaths = function (root) {
  const paths = [];
  const DFS = (root, path = "") => {
    if (!root) return;
    path += root.val;
    if (!root.left && !root.right) {
      paths.push(path);
      return;
    }
    path += "->";
    DFS(root.left, path);
    DFS(root.right, path);
  };
  DFS(root);
  return paths;
};
