var postorder = function (root) {
  if (!root) return [];
  const result = [];
  const DFS = (root) => {
    if (!root) return;
    for (const child of root.children) {
      DFS(child);
    }
    result.push(root.val);
  };
  DFS(root);
  return result;
};

//
