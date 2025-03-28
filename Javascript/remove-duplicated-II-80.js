var removeDuplicates = function (nums) {
  let encountered = {};
  encountered[nums[0]] = 1;
  let i = 1;
  while (i < nums.length) {
    if (encountered[nums[i]] > 1) {
      nums.splice(i, 1);
      continue;
    }
    encountered[nums[i]] ? encountered[nums[i]]++ : (encountered[nums[i]] = 1);
    i++;
  }
  console.log(nums);
};

removeDuplicates([1, 1, 1, 2, 2, 3]);
removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]);
// Given a sorted array of nums
// declare a hash map called encountered with a key equal to the first element and the value equal to 1
// declare a variable index set to 0
// loop through the array until index equals the nums length
// for each element
// if the element count is bigger than 1 remove the element and continue
// if the key exists add one to the value
// otherwise create the key
// Add 1 to the index variable
