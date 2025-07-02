var cloneGraph = function (node) {
  if (!node) return;
  const visited = new Set();
  visited.add(node.val);
  const queue = [node];
  const copy = [];
  while (queue.length) {
    const myNode = queue.shift();
    const freshCopy = new _Node(myNode.val);
    for (const neighbor of myNode.neighbors) {
      if (!visited.has(neighbor.val)) queue.push(neighbor);
      visited.add(neighbor.val);
      myNode.neighbors.push(new _Node(neighbor.val));
    }
  }
  console.log(copy);
};

// Traverse the graph BFS style
// Each time create new node
