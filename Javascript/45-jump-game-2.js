var jump = function (nums) {
  const n = nums.length;
  if (n < 2) return 0;
  let numJumps = 0;
  let currentIndex = 0;
  while (currentIndex + nums[currentIndex] < n - 1) {
    const jumpSize = nums[currentIndex];
    const possibleJumps = nums.slice(
      currentIndex + 1,
      currentIndex + jumpSize + 1
    );
    const bestSpot = possibleJumps.reduce(
      (acc, curr, idx) => {
        return acc[0] + acc[1] > curr + idx + currentIndex + 1
          ? acc
          : [curr, idx + currentIndex + 1];
      },
      [possibleJumps[0], currentIndex + 1]
    );
    currentIndex = bestSpot[1];
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
