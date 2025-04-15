const sortNumbers = (a, b) => a - b;

var longestConsecutive = function (nums) {
  const n = nums.length;
  if (n < 2) return n;
  const sorted = nums.sort(sortNumbers);
  let maxSequence = 0;
  let currentSequence = 1;
  for (let i = 1; i < n; i++) {
    console.log(sorted[i - 1] + 1 === sorted[i]);
    if (sorted[i - 1] === sorted[i]) continue;
    if (sorted[i - 1] + 1 === sorted[i]) {
      currentSequence++;
      continue;
    }
    if (currentSequence > maxSequence) maxSequence = currentSequence;
    currentSequence = 1;
  }
  return currentSequence > maxSequence ? currentSequence : maxSequence;
};

console.log(longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]));
// console.log(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]));
// console.log(longestConsecutive([100, 4, 200, 1, 3, 2]));

// Algo longestConsecutive
// Sort the array based on which number is bigger
// declare a variable maxSequence with initial value of 0
// declare a variable currentSequence with an initial value of 0
// iterate through the array from index 1
// compare the current number to the previous one
// if the number is the same go to the next number
// if the number is bigger by one add 1 to the currentSequence
// otherwise check if the currentSequence is bigger than the maxSequence
// if it ise maxSequence gets currentSequence
// in any case currentSequence gets 0
// after iteration return maxSequence
