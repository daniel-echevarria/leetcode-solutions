var lengthOfLongestSubstring = function (s) {
  const n = s.length;
  if (n < 2) return n;
  let left = 0;
  let right = 1;
  let longestSub = 1;
  let window;
  while (true) {
    window = s.substring(left, right);
    console.log(window);
    if (window.includes(s[right])) {
      const leftPart = s.substring(0, right);
      left = leftPart.lastIndexOf(s[right]) + 1;
      right++;
    } else {
      right++;
      longestSub = Math.max(longestSub, right - left);
    }
    if (right + 1 > s.length) return longestSub;
  }
};

console.log(lengthOfLongestSubstring("abcabcbb"));
console.log(lengthOfLongestSubstring("pwwkew"));
console.log(lengthOfLongestSubstring("bbtablud"));
// Given a string s, find the length of the longest substring without duplicate characters.

// Algo
// Declare a variable left with an initial value of 0
// Declare a variable right with an initial value of 1
// declare a variable longest with an initial value of 0
// declare a variable window that gets s.substring(left, right)
// launch a loop that never stops
// if the window includes s[right]
// left gets + 1
// if not
// declare a currentLength that gets right minus left
// if currentLength is longer than longest update longest
// in any case right gets + 1
// if right + 1 > s.length return longest
