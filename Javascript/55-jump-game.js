const canJump = (nums) => {
  let biggestJump = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i] === 0) {
      if (biggestJump <= i) return false;
    }
    const totalJump = nums[i] + i;
    if (totalJump > biggestJump) biggestJump = totalJump;
  }
  return true;
};

canJump2([2, 3, 1, 1, 4]);
canJump2([3, 2, 1, 0, 4]);

// New Algo:
// Given an array of numbers
// declare a variable biggestJump with a value of 0
// iterate through the array until the before last element
// if the current value is 0
// check if biggestJump is bigger than the current index
// if it's not return false
// if the current value + the current index is bigger than the biggestJump
// update biggestJump with the current value + index
// return true
