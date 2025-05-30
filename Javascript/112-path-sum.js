// var hasPathSum = function (root, targetSum) {
//   let hasTargetSum = false;
//   const DFS = (root, sum = 0) => {
//     if (hasTargetSum) return;
//     if (!root) return;
//     sum = sum + root.val;
//     if (!root.left && !root.right && sum === targetSum) {
//       hasTargetSum = true;
//       return;
//     }

//     DFS(root.left, sum);
//     DFS(root.right, sum);
//   };
//   DFS(root);
//   return hasTargetSum;
// };

var hasPathSum = function (root, targetSum) {
  if (!root) return false;
  targetSum = targetSum - root.val;
  if (!root.left && !root.right && targetSum == 0) return true;
  const left = hasPathSum(root.left, targetSum);
  const right = hasPathSum(root.right, targetSum);
  return left || right;
};

// Algo
// Declare a variable hasTargetSum with initial value of false
// Traverse the tree DFS style (recursion)
// If hasTargetSum is true return
// If root is null return
// While going down pass the sum of the ancestors
// When reaching a leaf check if the sum matches the targetSum if it does hasTargetSum gets true
// return hasTargetSum
