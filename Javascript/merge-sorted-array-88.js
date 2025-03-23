const merge = function (nums1, m, nums2, n) {
  for (let i = 0; i < m + n; i++) {
    if (nums1[i] >= nums2[0]) {
      nums1.splice(i, 0, nums2.shift());
      nums1.splice(-1);
    }
  }
  const rest = nums2.length;
  nums1.splice(-rest, rest, ...nums2);
};
