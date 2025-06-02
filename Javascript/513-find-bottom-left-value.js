var findBottomLeftValue = function (root) {
  let queue = [root];
  let lefMost = root.val;
  while (queue.length) {
    const row = [];
    for (const node of queue) {
      node.left && row.push(node.left);
      node.right && row.push(node.right);
    }
    if (row.length) lefMost = row[0].val;
    queue = [];
    queue.push(...row);
  }
  return lefMost;
};
