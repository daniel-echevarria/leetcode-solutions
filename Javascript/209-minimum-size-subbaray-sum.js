var minSubArrayLen = function (target, nums) {
  if (nums.reduce((acc, curr) => acc + curr) < target) return 0;
  const single = nums.find((x) => x >= target);
  if (single) return 1;
  const n = nums.length;
  let left = 0;
  let right = 1;
  let minLength = nums.length;
  let window = nums.slice(left, right);
  let sum = window[0];
  while (true) {
    if (sum < target) {
      if (right === n) return minLength;
      sum += nums[right];
      right++;
    }
    if (sum >= target) {
      minLength = Math.min(minLength, right - left);
      if (minLength === 2) return minLength;
      sum -= nums[left];
      left++;
    }
  }
};

console.log(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]));
console.log(minSubArrayLen(4, [1, 4, 4]));
console.log(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]));
console.log(minSubArrayLen(7, [7, 1, 1, 1]));

// Given an target and an array of numbers
// declare a constant n that gets the nums.length
// declare a variable l with initial value of 0
// declare a variable r with initial value of 0
// declare a variable minLength with an initial value n
// declare a variable currentSum with an initial value of nums[0]
// launch a loop that goes forever
// if the currentSum is smaller than the target
// add nums[r] to the current sum
// r gets +1
// if the currentSum is equal or bigger than the target
// declare a currentLength that gets left minus right
// minLength gets the smallest of minLength or currentLength

// return minLength
