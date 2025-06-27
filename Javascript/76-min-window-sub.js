var minWindow = function (s, t) {
  const n = s.length;
  const m = t.length;
  if (n < m) return "";
  if (s == t) return t;
  let l = 0;
  let r = 0 + m;
  let minWindowSize = s.length;
  let minWindow = "";
  let myMap = new Map();
  for (let i = 0; i < n; i++)
    myMap.get(s[i]) ? myMap.get(s[i]).push(i) : myMap.set(s[i], [i]);
  const sArray = s.split("");
  while (l < n) {
    const window = sArray.slice(l, r);
    let allInclusive = true;
    for (let char of t) {
      console.log(char);
      const indexes = myMap.get(char);
      console.log(indexes);
      const possibles = indexes.filter((idx) => idx >= l && idx <= r);
      console.log(possibles);
      if (indexes.length == 0) allInclusive = false;
      // if (window.includes(char)) {
      //   const idx = window.indexOf(char);
      //   window[idx] = "#";
      //   continue;
      // }
      // allInclusive = false;
    }
    if (allInclusive && window.length <= minWindowSize) {
      minWindow = s.slice(l, r);
      minWindowSize = window.length;
    }
    allInclusive ? l++ : r++;
    if (r == n + 1 && !allInclusive) break;
  }
  return minWindow;
};
