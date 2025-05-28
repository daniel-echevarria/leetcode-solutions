// var findSecondMinimumValue = function (root) {
//   if (!root || (!root.right && !root.left)) return -1;
//   const firstMin = root.val;
//   const secondMin = Math.max(root.right.val, root.left.val);
//   return firstMin < secondMin ? secondMin : -1;
// };

const findSecondMinimumValue = (root) => {
  const stored = [];
  const firstMin = root.val;
  const DFS = (root) => {
    if (!root) return;
    if (root.val != firstMin) stored.push(root.val);
    DFS(root.left);
    DFS(root.right);
  };
  DFS(root);
  stored.sort((a, b) => a - b);
  return stored[0] || -1;
};

// Operate a tree traversal and store all the values
// sort the values
// filter the values which are the same than the root
// return the  first value of stored
