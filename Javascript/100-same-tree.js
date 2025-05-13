var isSameTree = function (p, q) {
  if (!p && !q) return true;
  if (p && !q) return false;
  if (q && !p) return false;
  return (
    p.val === q.val &&
    isSameTree(p.left, q.left) &&
    isSameTree(p.right, q.right)
  );
};

// Given two root nodes of binary trees
// if the value of p is not the same than the value of q return false
// return the answer
