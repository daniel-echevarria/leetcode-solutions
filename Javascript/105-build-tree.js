var buildTree = function (preorder, inorder) {
  if (inorder.length === 0) return null;
  const rootVal = preorder.shift();
  const idx = inorder.indexOf(rootVal);
  const root = new TreeNode(rootVal);
  root.left = buildTree(preorder, inorder.slice(0, idx));
  root.right = buildTree(preorder, inorder.slice(idx + 1));
  return root;
};
