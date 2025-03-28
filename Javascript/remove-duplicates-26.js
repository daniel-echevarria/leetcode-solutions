// var removeDuplicates = function (nums) {
//   let removedCount = 0;
//   for (let i = 1; i < nums.length; i++) {
//     let a = nums[i];
//     let b = nums[i - 1];
//     console.log(a, b);
//     if (nums[i] === nums[i - 1]) {
//       nums[i] = "_";
//       removedCount++;
//     }
//   }
//   return nums.length - removedCount;
// };

const removeDuplicates = (nums) => {
  const encounteredValues = [nums[0]];
  let i = 1;
  while (i < nums.length) {
    if (encounteredValues.includes(nums[i])) {
      nums.splice(i, 1);
      continue;
    }
    encounteredValues.push(nums[i]);
    i++;
  }
  return nums.length;
};

removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]);

// Given an array ov values
// declare a removedElementsCount with a value of 0
// iterate through the array from the second element
// if the current element equals the previous element
// replace that element with a _
// add 1 to the removedElementsCount
// after iterating through the array
// return nums.length - remmovedElementsCount

// Given an array of values called nums,
// declare an encounteredValues array and push the first value of nums
// declare a variable i with a value of 1
// loop through nums
// if the value at index i is included in encounteredValues
// remove that value from nums and go to the next iteration
// otherwise add 1 to i
// if i equals nums.length exit the loop
// return nums length
