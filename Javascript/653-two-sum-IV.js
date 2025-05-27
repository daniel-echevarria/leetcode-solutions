var findTarget = function (root, k) {
  const myMap = new Map();
  let pairExists = false;
  const DFS = (root) => {
    if (!root || pairExists) return;
    const pair = myMap.get(k - root.val);
    if (pair) {
      pairExists = true;
      return;
    }
    myMap.set(root.val, true);
    DFS(root.left);
    DFS(root.right);
  };
  DFS(root);
  return pairExists;
};

// Declare an empty hash map
// Traverse the tree DFS style
// At each stage check if k - the current value is a key of the hash map
// If it is return true otherwise store the current value as a key and keep going
