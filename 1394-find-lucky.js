var findLucky = function (arr) {
  let largest = -1;
  const luckyCount = new Map();
  for (const el of arr) {
    luckyCount.set(el, (luckyCount.get(el) || 0) + 1);
  }
  for (const [key, val] of luckyCount) {
    if (Number(key) === val) largest = Math.max(largest, val);
  }
  return largest;
};
