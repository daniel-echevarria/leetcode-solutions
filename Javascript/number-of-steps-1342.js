var numberOfSteps = function (num) {
  const countSteps = (currentNum = num, currentSteps = 0) => {
    if (currentNum === 0) return currentSteps;
    currentNum = currentNum % 2 === 0 ? currentNum / 2 : currentNum - 1;
    currentSteps += 1;
    return countSteps(currentNum, currentSteps);
  };
  return countSteps();
};

const ex1 = numberOfSteps(14);
console.log(ex1);

// Algo
// Given a current number, and a number of steps equal to 0
// If the number is 0 return the number of steps
// Otherwise check if the number is even
// If it is divide it by 2
// If it is not take out 1
// Add a step
// Call the method if the new number and the current steps
