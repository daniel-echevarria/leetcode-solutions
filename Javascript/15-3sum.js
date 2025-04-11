function compareNumbers(a, b) {
  return a - b;
}

var threeSum = function (nums) {
  const n = nums.length;
  const triplets = [];
  let i = 0;
  let j = 1;
  let k = n - 1;
  nums = nums.sort(compareNumbers);
  while (i < k) {
    const currentTriplet = [nums[i], nums[j], nums[k]].sort(compareNumbers);
    const sum = currentTriplet.reduce((a, b) => a + b);
    const tripletAlreadyExists = triplets.some((triplet) =>
      triplet
        .sort(compareNumbers)
        .every((val, index) => val === currentTriplet[index])
    );

    if (sum === 0 && !tripletAlreadyExists) triplets.push(currentTriplet);
    if (sum > 0) k--;
    if (sum <= 0) j++;
    if (j >= k) {
      i++;
      j = i + 1;
    }
  }
  return triplets;
};

// Given an array of numbers find all the triplets that add to 0
// declare a triplets empty array
// declare a variable i with initial value of 0
// declare a variable j with an initial value of 1
// declare a variable k with initial value of nums.length - 1
// nums gets nums sorted
// launch a loop that stops when i is bigger or equal to k
// declare a sum of values nums[i], nums[j] and nums[k]
// if the sum is bigger than 0 k gets minus 1
// if the sum is smaller or equal to 0 j gets plus 1
// if j equals k
// i gets + 1 and j gets i + 1

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
console.log(threeSum([0, 1, 1]));
console.log(threeSum([0, 0, 0]));
console.log(
  threeSum([2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10])
);
// console.log(threeSum())
