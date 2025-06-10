var flatten = function (root) {
  const preOrder = [];
  const DFS = (node) => {
    if (!node) return;
    preOrder.push(node);
    DFS(node.left);
    DFS(node.right);
  };
  DFS(root);
  for (let i = 0; i < preOrder.length; i++) {
    const currentNode = preOrder[i];
    currentNode.left = null;
    currentNode.right = i < preOrder.length - 1 ? preOrder[i + 1] : null;
  }
  return root;
};

// const flatten = (root) => {
//   const DFS = (node) => {
//     if (!node) return;
//     if (node.left.left === null && node.left.rightl)
//   };
// };

// If the left node is a leaf
// store the right node in a tempo
// right gets left
// left gets null
// right right gets tempo
// otherwise call flatten on the left
// call flatten on the right
