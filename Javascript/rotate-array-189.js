const rotate = (nums, k) => {
  const shift = k % nums.length;
  const rotating = nums.splice(-shift);
  nums.splice(0, 0, ...rotating);
};

rotate([1, 2, 3, 4, 5, 6, 7], 3);
