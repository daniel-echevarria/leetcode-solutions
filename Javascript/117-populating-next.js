var connect = function (root) {
  if (!root) return root;
  const queue = [root];
  while (queue.length) {
    const size = queue.length;
    const nextRow = [];
    for (let i = 0; i < size; i++) {
      const node = queue.shift();
      if (queue.length) node.next = queue[0];
      node.left && nextRow.push(node.left);
      node.right && nextRow.push(node.right);
    }
    queue.push(...nextRow);
  }
  return root;
};

// Use BFS
// At each stage, shift and point to the next
// If it's empty point to null
