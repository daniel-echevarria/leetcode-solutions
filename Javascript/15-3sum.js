var threeSum = function (numbers) {
  const n = numbers.length;
  const nums = numbers.sort((a, b) => a - b);
  let i = 0;
  let j = 1;
  let k = n - 1;
  const triplets = new Map();
  while (i < n) {
    while (j < k) {
      const total = nums[i] + nums[j] + nums[k];
      const triplet = [nums[i], nums[j], nums[k]];
      if (total == 0) triplets.set(triplet.sort().toString(), triplet);
      if (total <= 0) {
        const tempo = j;
        while (nums[j] == nums[tempo]) j++;
      } else k--;
    }
    i++;
    j = i + 1;
    k = n - 1;
  }
  return [...triplets.values()];
};
