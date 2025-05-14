const invertTree = (root) => {
  if (!root) {
    return null;
  }
  [root.left, root.right] = [root.right, root.left];
  invertTree(root.left);
  invertTree(root.right);
  return root;
};

const isSameTree = (p, q) => {
  if (!p && !q) return true;
  if (p && !q) return false;
  if (!p && q) return false;
  return (
    p.val === q.val &&
    isSameTree(p.left, q.left) &&
    isSameTree(p.right, q.right)
  );
};

var isSymmetric = function (root) {
  const right = invertTree(root.right);
  return isSameTree(root.left, right);
};

const areSymmetric = (p, q) => {
  if (!p && !q) return true;
  if (p && !q) return false;
  if (!p && q) return false;
  return (
    p.val === q.val &&
    areSymmetric(p.left, q.right) &&
    areSymmetric(p.right, q.left)
  );
};

const isSymmetric = (root) => {
  return areSymmetric(root.left, root.right);
};

// Algo isSymmetric
// Given the root of a binary tree
// Recursively revert the right child
// check if the tree are the same

// given two roots
// they are symetrical if
// the left child of p equals the right child of q
// and the right child of p equals the left child of q
// and if calling that with the left child of p and the right child of q
// and calling it with the right child of p and the left child of q is also true
