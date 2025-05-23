const isSameTree = (a, b) => {
  if (!a && !b) return true;
  if (a && !b) return false;
  if (!a && b) return false;
  return (
    a.val === b.val &&
    isSameTree(a.left, b.left) &&
    isSameTree(a.right, b.right)
  );
};

var isSubtree = function (root, subRoot) {
  if (!root) return;
  let isSubtree = false;
  const BFS = (root) => {
    if (!root) return;
    if (isSameTree(root, subRoot)) {
      isSubtree = true;
      return;
    }
    BFS(root.left);
    BFS(root.right);
  };
  BFS(root);
  return isSubtree;
};
