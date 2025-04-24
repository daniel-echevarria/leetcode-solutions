var isValid = function (s) {
  const hash = {
    "]": "[",
    "}": "{",
    ")": "(",
  };
  const stack = [];
  for (let i = 0; i < s.length; i++) {
    const currentChar = s[i];
    if (hash[currentChar]) {
      if (stack[stack.length - 1] === hash[currentChar]) {
        stack.pop();
        continue;
      }
      return false;
    }
    stack.push(currentChar);
  }
  return stack.length === 0;
};

// Algo
// Given a string of parentheses
// declare a map that maps each closing parentheses to it's opening
// declare an array of the closing parentheses [}])]
// declare a variable stack with initial value of []
// iterate through the string
// push to the stack until meeting a closing parentheses
// when meeting a closing parentheses check if the last value of the stack
// matches the value from the map for this closing parentheses
// if they do, pop the last value from the stack
// if they don't return false
// after iteration return true if stack is empty or false if not

console.log(isValid("([])"));
