const isSameTree = (a, b) => {
  if (a === null && b === null) return true;
  if (a && b === null) return false;
  if (a === null && b) return false;
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
    if (isSameTree(root, subRoot)) isSubtree = true;
    BFS(root.left);
    BFS(root.right);
  };
  BFS(root);
  return isSubtree;
};

// Algo
// Use BFS and compare the current val to the subRoot val
// if they are the same recursively compare the values of all the descendents
//
