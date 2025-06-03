var findBottomLeftValue = function (root) {
  let queue = [root];
  let lefMost = root.val;
  while (queue.length) {
    lefMost = queue[0].val;
    const len = queue.length;
    for (let i = 0; i < len; i++) {
      const node = queue.shift();
      node.left && queue.push(node.left);
      node.right && queue.push(node.right);
    }
  }
  return lefMost;
};
