var inorderTraversal = function (root) {
  const visited = [];
  const DFS = (root) => {
    if (!root) return;
    if (root.left) DFS(root.left);
    visited.push(root.val);
    if (root.right) DFS(root.right);
  };
  DFS(root);
  return visited;
};

const visited = [];
const iterative = (root) => {
  let keepGoing = true;
  let curr = root;
  let prev = root;
  while (keepGoing) {
    let left = curr.left;
    let right = curr.right;
    if (!left && !right) {
      visited.push(curr.val);
    }
    if (left) {
      curr = left;
      continue;
    }
  }
};
// Given the root of a tree give it's inorder traversal
// Declare a variable visited that gets an empty array
// If the root is a leaf (left is null and right is null)
// push the value of the root to the visited array
// if there is a left branch call inorder on it
// if there is a right branch call inorder on it
// return the visited array
