var sortedArrayToBST = function (nums) {
  if (nums.length === 0) return null;
  const rootIndex = Math.floor(nums.length / 2);
  const rootValue = nums[rootIndex];
  const root = new TreeNode(rootValue);
  const leftNums = nums.slice(0, rootIndex);
  const rightNums = nums.slice(rootIndex + 1);
  root.left = sortedArrayToBST(leftNums);
  root.right = sortedArrayToBST(rightNums);
  return root;
};

// Algo
// Find the middle of the array
// That becomes the root node
// the left child gets the result of calling
