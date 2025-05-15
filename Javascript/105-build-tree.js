// var buildTree = function (preorder, inorder) {
//   const myTree = new TreeNode(null);
//   for (value of preorder) placeValue(value, myTree, inorder);
//   return myTree;
// };

// const placeValue = (value, currentNode, inorder) => {
//   if (currentNode.val === null) {
//     currentNode.val = value;
//     return;
//   }
//   if (inorder.indexOf(value) < inorder.indexOf(currentNode.val)) {
//     currentNode.left
//       ? placeValue(value, currentNode.left, inorder)
//       : (currentNode.left = new TreeNode(value));
//   } else {
//     currentNode.right
//       ? placeValue(value, currentNode.right, inorder)
//       : (currentNode.right = new TreeNode(value));
//   }
// };

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

var buildTree = function (preorder, inorder) {};

// given two lists of values
// take the first value of preorder that is the root
// the values before in inorder are leftvalues the values after are right values
// call placeValues on the left child with the left values
// call placeValues on the right child with the right values
