var buildTree = function (inorder, postorder) {
  const build = (array) => {
    if (postorder.length === 0) return null;
    if (array.length === 0) return null;
    const value = postorder.pop();
    const idx = array.indexOf(value);
    const node = new TreeNode(value);
    node.right = build(array.slice(idx + 1));
    node.left = build(array.slice(0, idx));
    return node;
  };
  return build(inorder);
};
