// const nodes = [];
// const queue = [];

// var connect = function (root) {
//   if (!root) return;
//   nodes.push(queue.pop());
//   queue.unshift(root.left);
//   queue.unshift(root.right);
//   connect(root.left);
//   connect(root.right);
// };

const visited = [];
const queue = [];

const connect = (root) => {
  if (!root) return;
  visited.push(queue.pop());
  queue.push(root.right);
  queue.push(root.left);
  connect(root.left);
  connect(root.right);
  console.log(visited);
};
