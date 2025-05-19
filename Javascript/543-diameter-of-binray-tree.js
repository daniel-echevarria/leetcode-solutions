// algo
// declare a variable maxDiam with initial value of 0
// find the longestPath on the left node
// find the longestPath on the right node
// Add the two path and if they are bigger than maxDiam update maxDiam

// Algo longestPath
// Declare a variable longest with initial value of 0
// Given a root
// if the root is null return longest
// longest gets + 1
// declare a variable longestLeft that gets calling longestPath on the left child
// declare a variable longestRight that gets calling longestPath on the right child
// longestPath gets the max longestLeft and longestRight
// return longest

const maxDepth = (root) => {
  if (!root) return 0;
  if (!root.left && !root.right) return 1;
  const maxLeft = root.left ? 1 + maxDepth(root.left) : 0;
  const maxRight = root.right ? 1 + maxDepth(root.right) : 0;
  return Math.max(maxLeft, maxRight);
};

const getDiam = (root) => {
  if (!root) return 0;
  const longestLeft = root.left ? maxDepth(root.left) : 0;
  const longestRight = root.right ? maxDepth(root.right) : 0;
  return longestLeft + longestRight;
};

var diameterOfBinaryTree = function (root) {
  if (!root) return 0;
  let maxDiam = 0;
  const getMaxDiam = (root) => {
    const maxLeft = getDiam(root.left);
    const maxRight = getDiam(root.right);
    const current = getDiam(root);
    maxDiam = Math.max(maxLeft, maxRight, current, maxDiam);
  };
  if (root.left) getMaxDiam(root.left);
  if (root.right) getMaxDiam(root.right);
  getMaxDiam(root);
  return maxDiam;
};

// Algo diameter
// get the maxDiameter from the left child
//
// get the maxDiameter from the right chid
// get the diameter of the current node
// return the biggest of the 3 results
