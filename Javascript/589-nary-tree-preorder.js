var preorder = function (root) {
  const result = [];
  const DFS = (root) => {
    if (!root) return;
    result.push(root.val);
    for (const child of root.children) {
      DFS(child);
    }
  };
  DFS(root);
  return result;
};

// Visit the parent visit the children recursively
