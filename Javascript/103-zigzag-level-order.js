var zigzagLevelOrder = function (root) {
  if (!root) return [];
  let queue = [root];
  let result = [];
  let count = 0;
  while (queue.length) {
    const levelValues = queue.map((node) => node.val);
    count % 2 === 0
      ? result.push(levelValues)
      : result.push(levelValues.reverse());
    const nextLevel = [];
    for (const node of queue) {
      node.left && nextLevel.push(node.left);
      node.right && nextLevel.push(node.right);
    }
    queue = nextLevel;
    count++;
  }
  return result;
};

// Traverse the tree BFS
// use a count to go from right to left if the level is even
