var countNodes = function (root) {
  if (!root) return 0;
  let numNodes = 0;
  const DFS = (root) => {
    if (!root) return;
    numNodes++;
    DFS(root.left);
    DFS(root.right);
  };
  DFS(root);
  return numNodes;
};
