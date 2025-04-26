const applyOperation = (operation, a, b) => {
  return operation(a, b);
};

var evalRPN = function (tokens) {
  const hash = {
    "+": (a, b) => a + b,
    "-": (a, b) => a - b,
    "*": (a, b) => a * b,
    "/": (a, b) => {
      const result = a / b;
      return result > 0 ? Math.floor(result) : Math.ceil(result);
    },
  };
  const stack = [];
  for (const t of tokens) {
    console.log(stack, t);
    if (hash[t]) {
      const right = stack.pop();
      const left = stack.pop();
      stack.push(applyOperation(hash[t], left, right));
      console.log(stack);
      continue;
    }
    stack.push(+t);
  }
  return stack[0];
};

// Algo
// Declare an map with all the operators +, -, /, * strings maped to the operators
// Declare a variable result with an initial value of 0
// declare a constant stack that gets []
// Iterate through the tokens
// If the token is a key of the map
// pop the last value of the stack and give it to right
// pop the last value of the stack and give it to left
// Add the result of right token left to the result
// after iteration return result

// console.log(evalRPN(["2", "1", "+", "3", "*"]));
// console.log(evalRPN(["4", "13", "5", "/", "+"]));
console.log(
  evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
);
