var MinStack = function () {
  const myStack = {
    stack: [],
    push: (val) => myStack["stack"].push(val),
    getMin: () => Math.min(...myStack["stack"]),
    top: () => myStack["stack"][myStack["stack"].length - 1],
    pop: () => myStack["stack"].pop(),
  };
  return myStack;
};

var obj = new MinStack();
obj.push(3);
obj.push(1);
console.log(obj.getMin());
obj.pop();
var param_3 = obj.top();
var param_4 = obj.getMin();
