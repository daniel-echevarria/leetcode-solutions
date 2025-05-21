var findTilt = function (root) {
  if (!root) return 0;

  const tilt = (node) => {
    if (!node) return 0;
    const left = tilt(node.left);
    const right = tilt(node.right);
    const absDiff = Math.abs(left - right);
    const tempo = node.val;
    node.val = absDiff;
    return left + right + tempo;
  };

  tilt(root);

  const sum = (root) => {
    if (!root) return 0;
    const left = sum(root.left);
    const right = sum(root.right);
    return left + right + root.val;
  };

  return sum(root);
};

// Algo
// Get the sum of the left node
// Get the sum of the right node
// get the absolute difference and store it in a variable absDiff
// store the current root value in a tempo
// the current root value gets absDiff
// return the sum of the left node plus the sum of the right node plus the tempo
