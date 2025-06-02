var leafSimilar = function (root1, root2) {
  const DFS = (root, string = "") => {
    if (!root) return string;
    if (!root.left && !root.right) return string + root.val + "#";
    const left = DFS(root.left, string);
    const right = DFS(root.right, string);
    return left + right;
  };
  const string1 = DFS(root1);
  const string2 = DFS(root2);
  return string1 === string2;
};
