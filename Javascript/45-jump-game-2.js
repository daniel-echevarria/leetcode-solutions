var jump = function (nums) {
  let numJumps = 0;
  let currentIndex = 0;
  let bestJumpIndex = 0;
  if (nums.length < 2) return numJumps;
  let bestJumpValue = 0;

  while (nums[currentIndex] + currentIndex < nums.length - 1) {
    for (let j = 1; j <= nums[currentIndex]; j++) {
      if (nums[currentIndex + j] + currentIndex + j >= bestJumpValue) {
        bestJumpValue = nums[currentIndex + j];
        bestJumpIndex = currentIndex + j;
      }
    }
    currentIndex = bestJumpIndex;
    numJumps++;
  }
  console.log(numJumps);
  return numJumps;
};

jump([2, 3, 1, 1, 4]);
jump([1, 1, 1, 1]);
jump([1, 2, 1, 1, 1]);
jump([0]);

// Given an array of numbers
// declare numJumps with an initial value of 1
// declare currentIndex with an initial value of 0
// declare bestJumpValue with an initial value of nums[currentIndex]
// declare bestJumpIndex
// if currentIndex = nums.length - 1 return numJumps
// loop through the possible jumps and find the biggest value
// bestJumpValue gets that value and bestJumpIndex gets that index
// after the loop currentIndex gets bestJumpIndex
// add 1 to numJumps
