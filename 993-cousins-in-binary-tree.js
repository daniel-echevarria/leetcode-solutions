var isCousins = function (root, x, y) {
  const visited = [];
  const queue = [root];
  const DFS = (root) => {
    if (!root) return;
    visited.push(queue.shift().val);
    root.left && queue.push(root.left);
    root.right && queue.push(root.right);
    DFS(root.left);
    DFS(root.right);
  };
  DFS(root);
};

// Given the root of a binary tree and two nodes on that tree x and y
// tell if the nodes ares cousins (different parents but same generation/level)
// Algo:
// Declare a string visited
// Iterate through the array DFS
// adding the visited values to the string
// when changing levels add # to the string
// after visiting the tree
// split the string at #
// find the array containing x and check if it also contains y
