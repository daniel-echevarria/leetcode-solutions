const biggestValue = (root) => {
  if (!root.right) return root.val;
  return biggestValue(root.right);
};

const smallestValue = (root) => {
  if (!root.left) return root.val;
  return smallestValue(root.left);
};

var getMinimumDifference = function (root) {
  if (!root) return;
  const maxDiff = 100000;
  let minAbsDiff = maxDiff;
  const DFS = (root) => {
    if (!root) return;
    const absDiffLeft = root.left
      ? Math.abs(root.val - biggestValue(root.left))
      : maxDiff;
    const absDiffRight = root.right
      ? Math.abs(root.val - smallestValue(root.right))
      : maxDiff;
    minAbsDiff = Math.min(absDiffLeft, absDiffRight, minAbsDiff);
    DFS(root.left);
    DFS(root.right);
  };
  DFS(root);
  return minAbsDiff;
};

// Algo
// Declare a variable minAbsDiff with an initial value of 100 000
// Compare the absolute value of the root.val minus the biggestValue on the left child
// minAbsDiff gets the smallest value between the result and the current minAbsDiff
// Compare the absolute value of the root.val minus the smallestValue on the right child
// minAbsDiff gets the smallest value between the result and the current minAbsDiff
// call it on the left node
// call it on the right node
// after the traversal return minAbsDiff

// Algo findBiggestValue
// Given a root if it has no right child return the current value
// otherwise call it on right child
