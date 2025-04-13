const compareNumbers = (a, b) => {
  return a - b;
};

var twoSum = function (nums, target) {
  const n = nums.length;
  let i = 0;
  let j = n - 1;
  const sorted = nums.toSorted(compareNumbers);
  while (i < n) {
    const l = sorted[i];
    const r = sorted[j];
    const sum = l + r;
    if (sum === target) return [nums.indexOf(l), nums.lastIndexOf(r)];
    sum > target ? j-- : i++;
  }
};

console.log(twoSum([2, 7, 11, 15], 9));
console.log(twoSum([-1, -2, -3, -4, -5], -8));

// give an array of numbers and a target number
// find the indexes of the two numbers that add to the target

// Algo
// declare a variable i with initial value of 0
// declare a variable j with initial value of nums.length -1
// Iterate through nums and for each value map it into an hash to it's index
// Then  sort the array of numbers
// Launch a loop that loops while i < n
// calculate the sum of nums[i] and nums[j]
// if the sum equals the target return the value of the hashMap for the key i and j
// if the sum is bigger than the target
// j gets - 1
// if the sum is smaller than the target
// i gets + 1
