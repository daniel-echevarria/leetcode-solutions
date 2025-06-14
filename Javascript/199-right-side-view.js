var rightSideView = function (root) {
  if (!root) return [];
  let queue = [root];
  const result = [];
  while (queue.length) {
    result.push(queue[queue.length - 1].val);
    const nextLevel = [];
    for (const node of queue) {
      node.left && nextLevel.push(node.left);
      node.right && nextLevel.push(node.right);
    }
    queue = [...nextLevel];
  }
  return result;
};
