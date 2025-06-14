var levelOrder = function (root) {
  if (!root) return [];
  let queue = [root];
  let result = [];
  while (queue.length) {
    const nextLevel = [];
    const level = [];
    for (const node of queue) {
      level.push(node.val);
      node.left && nextLevel.push(node.left);
      node.right && nextLevel.push(node.right);
    }
    result.push(level);
    queue = [...nextLevel];
  }
  return result;
};
