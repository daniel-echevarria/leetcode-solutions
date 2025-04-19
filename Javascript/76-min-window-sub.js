var minWindow = function (s, t) {
  const m = s.length;
  const n = t.length;
  let left = 0;
  let right = n;
  let minWindow = s;
  let encounteredAt = new Map();
  while (s.substring(left).length > n) {
    let allThere = false;
    const window = s.substring(left, right);
    for (let i = 0; i < n; i++) {
      const index = window.indexOf(encounteredAt.get(char) || 0);
      if (index === -1) {
        left++;
        encounteredAt = new Map();
        break;
      }
      encounteredAt.set(char, i + 1);
      if
    }
    console.log(allThere);
    if (allThere) {
      minWindow = window.length < minWindow.length ? window : minWindow;
      left++;
      continue;
    }
    right++;
  }
  return minWindow;
};

console.log(minWindow("ADOBECODEBANC", "ABC"));

// Algo
// m = s.length
// n = t.length
// declare a variable left with initial value of 0
// declare a variable right with initial value of n
// declare a variable minWindow with initial value of m
// declare a map encounteredAt
// declare a variable allThere with initial value of false
// split t into an array of characters
// launch a loop
// given a window which is a substring of s from left to right
// iterate through the characters
// find the index of the character in the window starting at the value from encounteredAt or 0
// if index is -1 stop iteration
// otherwise add that character as a key to encountered with a value of the index + 1
// after iteration allThere gets true
// if allThere is true minWindow gets the smallest of the two values minWindow or currentWindowLength
// and left gets ++
// otherwise
// right get ++
// stop the loop when the substring left to end is smaller than n
