var twoSum = function (numbers, target) {
  const n = numbers.length;
  let i = 0;
  let j = n - 1;
  let keepGoing = true;
  while (keepGoing) {
    currentSum = numbers[i] + numbers[j];
    if (currentSum === target) return [i + 1, j + 1];
    currentSum > target ? j-- : i++;
  }
};

console.log(twoSum([2, 7, 11, 15], 9));
console.log(twoSum([3, 24, 50, 79, 88, 150, 345], 200));
console.log(
  twoSum(
    [
      12, 13, 23, 28, 43, 44, 59, 60, 61, 68, 70, 86, 88, 92, 124, 125, 136,
      168, 173, 173, 180, 199, 212, 221, 227, 230, 277, 282, 306, 314, 316, 321,
      325, 328, 336, 337, 363, 365, 368, 370, 370, 371, 375, 384, 387, 394, 400,
      404, 414, 422, 422, 427, 430, 435, 457, 493, 506, 527, 531, 538, 541, 546,
      568, 583, 585, 587, 650, 652, 677, 691, 730, 737, 740, 751, 755, 764, 778,
      783, 785, 789, 794, 803, 809, 815, 847, 858, 863, 863, 874, 887, 896, 916,
      920, 926, 927, 930, 933, 957, 981, 997,
    ],
    542
  )
);

// Algo given an array of numbers and a target value
// Declare a variable i with initial value of 0
// Declare a variable j with initial value of numbers.length
// Declare a variable currentSum with initial value of 0
// Launch a loop that stops when numbers[i] + numbers[j] equals the target
// check if the current sum is bigger than the target
// if it is j gets -1
// if not i gets +1
