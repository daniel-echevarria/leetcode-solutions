var summaryRanges = function (nums) {
  const result = [];
  let rangeStart = nums[0];
  let currentRange = "";
  for (let i = 1; i < nums.length + 1; i++) {
    if (nums[i - 1] + 1 === nums[i]) continue;
    if (nums[i - 1] === rangeStart) {
      currentRange += nums[i - 1];
    } else {
      currentRange += rangeStart + "->" + nums[i - 1];
    }
    result.push(currentRange);
    currentRange = "";
    rangeStart = nums[i];
  }
  return result;
};

console.log(summaryRanges([-1]));
console.log(summaryRanges([0, 1, 2, 4, 5, 7]));
console.log(summaryRanges([0, 2, 3, 4, 6, 8, 9]));

// Algo
// declare a variable result with an initial value of []
// declare a variable rangeStart with an initial value of 0
// declare a variable i with an initial value of 1
// declare a variable currentRange with an initial value of ''
// Iterate through nums
// If nums[i - 1] + 1 is not equal to nums[i]
// check if  nums[i - 1] is equal to rangeStart
// if it is add nums[i - 1] to the currentRange
// otherwise add rangeStart + -> + nums[i - 1]
// push the string to the result array
// currentString gets ''
// rangeStart gets i
// i gets ++
// If it is
// i++
