var largestValues = function (root) {
  if (!root) return [];

  const res = [];
  const queue = [root];

  while (queue.length) {
    const size = queue.length;
    let max = -Infinity;

    for (let i = 0; i < size; i++) {
      const node = queue.shift();
      max = Math.max(max, node.val);
      node.left && queue.push(node.left);
      node.right && queue.push(node.right);
    }
    res.push(max);
  }
  return res;
};
