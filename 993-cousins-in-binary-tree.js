var isCousins = function (root, x, y) {
  const queue = [root];
  let xDepth;
  let yDepth;
  let sameParent = false;
  const DFS = (root, depth = 0) => {
    if (!root) return;
    if (root.val === x) xDepth = depth;
    if (root.val === y) yDepth = depth;
    root.left && queue.push(root.left);
    root.right && queue.push(root.right);
    if (root.left && root.right) {
      if (
        (root.left.val === x && root.right.val === y) ||
        (root.left.val === y && root.right.val === x)
      ) {
        sameParent = true;
      }
    }
    depth++;
    DFS(root.left, depth);
    DFS(root.right, depth);
  };
  DFS(root);
  if (sameParent) return false;
  return xDepth === yDepth;
};

// Given the root of a binary tree and the values of two nodes in the tree
// Traverse the tree BFS
// check if the root has a left child
// if it does check if the child has the value of x
// if it does xParent gets root
// check if the child has the value of y
// if it does yParent gets
