/**
 * @param {number[]} nums
 * @return {number[]}
 */
// var productExceptSelf = function (nums) {
//   const answer = nums.map((num, i) => {
//     const reduced = nums.reduce((acc, curr, j) => {
//       if (curr === 1 || i === j) return acc;
//       if (i === -1) return -acc;
//       return acc * curr;
//     }, 1);
//     return reduced;
//   });
//   console.log(answer);
//   return answer;
// };

// Given an array of numbers
// map each number to the product of all other numbers

// Simplify array first by removing all ones

const productExceptSelf = (nums) => {
  let left = 1;
  let right = 1;
  let answer = Array.from({ length: nums.length }, () => 1);

  for (let i = 0; i < nums.length; i++) {
    answer[i] = left * answer[i];
    left = left * nums[i];
  }
  for (let j = nums.length - 1; j > -1; j--) {
    answer[j] = right * answer[j];
    right = right * nums[j];
  }
  return answer;
};

productExceptSelf([1, 2, 3, 4]);
productExceptSelf([4, 3, 2, 1, 2]);

// Given an array of numbers
// create an array answer filled with ones
// iterate from the left of nums
// first multiply then answer to the left
// then update left bu multiplying to the current number
// do the same from the right side
