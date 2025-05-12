var isSameTree = function (p, q) {
  if (p.val !== q.val) return false;
  const resultLeft = isSameTree(p.left, q.left);
  const resultRight = isSameTree(p.right, q.right);
  return resultLeft && resultRight;
};

// Given two root nodes of binary trees
// if the value of p is not the same than the value of q return false
// return the answer
