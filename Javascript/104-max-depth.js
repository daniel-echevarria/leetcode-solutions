var maxDepth = function (root) {
  if (!root) return 0;
  const maxLeft = maxDepth(root.left);
  const maxRight = maxDepth(root.right);
  return 1 + Math.max(maxLeft, maxRight);
};
