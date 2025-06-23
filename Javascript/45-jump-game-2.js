var jump = function (nums) {
  const n = nums.length;
  if (n < 2) return 0;
  let numJumps = 0;
  let currentIndex = 0;
  while (currentIndex + nums[currentIndex] < n - 1) {
    const jumpSize = nums[currentIndex];
    const bestSpot = { index: 0, value: 0 };
    for (let i = currentIndex + 1; i <= currentIndex + jumpSize; i++) {
      if (i + nums[i] > bestSpot.value + bestSpot.index) {
        bestSpot.index = i;
        bestSpot.value = nums[i];
      }
    }
    currentIndex = bestSpot.index;
    numJumps++;
  }
  return numJumps + 1;
};

// Algo
// Declare a variable numJumps
// Declare a variable currentIndex with initial value of 0
// Loop until currentIndex equals nums[n - 1]
// Available jumpSize gets the value at the current index
// Iterate from current index to index plus availableJumpSize
// find the biggest value for index + value
// move the currentIndex to that index
// add 1 to numJumps
