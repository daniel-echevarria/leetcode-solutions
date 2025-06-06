var connect = function (root) {
  if (!root) return root;
  const queue = [root];
  while (queue.length) {
    const size = queue.length;
    for (let i = 0; i < size; i++) {
      const node = queue.shift();
      if (i < size - 1) node.next = queue[0];
      node.left && queue.push(node.left);
      node.right && queue.push(node.right);
    }
  }
  return root;
};
