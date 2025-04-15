var containsNearbyDuplicate = function (nums, k) {
  const hash = new Map();
  for (let i = 0; i < nums.length; i++) {
    const key = nums[i];
    if (hash.has(key)) {
      const abs = i - hash.get(key);
      if (abs <= k) return true;
      hash.set(key, i);
    } else {
      hash.set(key, i);
    }
  }
  return false;
};

console.log(containsNearbyDuplicate([1, 2, 3, 1], 3));
console.log(containsNearbyDuplicate([1, 0, 1, 1], 1));

// Given an array of numbers nums and an integer k
// Declare an hash map
// iterate through the nums
// for each number
// check if the key exists in the map
// if it does substract indexTotal from the current index
// if the result is smaller or equal to k return true
// if it does not add that key with a value of an object with 2 properties
// after iteration returns false
