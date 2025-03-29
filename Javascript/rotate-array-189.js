var rotate = function (nums, k) {
  const shift = k % nums.length;
  console.log(shift);
  for (let i = 0; i < shift; i++) {
    nums.unshift(nums.pop());
  }
  return nums;
};

const rotate2 = (nums, k) => {
  const shift = k % nums.length;
  const rotating = nums.splice(-shift);
  nums.splice(0, 0, ...rotating);
};

rotate([1, 2, 3, 4, 5, 6, 7], 3);

// Given an array and a number k
// create a for loop that starts at 0, finishes at k and increments 1 per round
// at each turn of the loop,
// declare a variable rotatingValue that gets the popped value from nums
// add that value to the start of nums
// return nums

// Given an array and a number k
// Slice the last part of the array at -k and store it in a variable rotating
// splice the array at the start of nums
