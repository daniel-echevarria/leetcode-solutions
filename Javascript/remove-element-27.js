var removeElement = function (nums, val) {
  let keepGoing = true;
  while (keepGoing) {
    let i = nums.indexOf(val);
    i === -1 ? (keepGoing = false) : nums.splice(i, 1);
  }
  return nums.length;
};
// given an array of values and a value
// create a loop that keeps looking for the index of the value
// if it finds an index, remove the element at that index
// when no more index are found
// exit the loop and return nums

const removeElement = (nums, val) => {
  let i = nums.indexOf(val);
  if (i === -1) return nums.length;
  nums.splice(i, 1);
  removeElement(nums, val);
};

// recursive remove element
// given an array ov values and a value
// look for the index of the value
// if the index === -1 return nums length
// otherwise remove the element at that index
// call the method again
removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2);
