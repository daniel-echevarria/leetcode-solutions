var lowestCommonAncestor = function (root, p, q) {
  let pPath = null;
  let qPath = null;
  let myMap = new Map();
  const DFS = (node, path = "") => {
    if (qPath && pPath) return;
    if (!node) return;
    myMap[node.val] = node;
    path += node.val.toString() + ",";
    if (node === p) pPath = path.split(",");
    if (node === q) qPath = path.split(",");
    DFS(node.left, path);
    DFS(node.right, path);
  };
  DFS(root);
  let lca = root.val;
  for (let i = 0; i < qPath.length; i++) {
    if (qPath[i] !== pPath[i]) break;
    lca = qPath[i];
  }
  return myMap[lca];
};
