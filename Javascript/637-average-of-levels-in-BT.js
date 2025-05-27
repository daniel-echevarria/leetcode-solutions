var averageOfLevels = function (root) {
  let queue = [root];
  const averages = [];
  while (queue.length > 0) {
    const sum = queue.reduce((acc, curr) => acc + curr.val, 0);
    const average = sum / queue.length;
    averages.push(average);
    const tempo = queue;
    queue = [];
    tempo.forEach((node) => {
      node.left && queue.push(node.left);
      node.right && queue.push(node.right);
    });
  }
  return averages;
};

var averageOfLevels = function (root) {
  let queue = [root];
  const averages = [];
  while (queue.length > 0) {
    let sum = 0;
    const queueLength = queue.length;
    for (let i = 0; i < queueLength; i++) {
      const currentNode = queue.shift();
      sum += currentNode.val;
      currentNode.left && queue.push(currentNode.left);
      currentNode.right && queue.push(currentNode.right);
    }
    averages.push(sum / queueLength);
  }
  return averages;
};
