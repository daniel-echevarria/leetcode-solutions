var strStr = function (haystack, needle) {
  for (i = 0; i < haystack.length; i++) {
    if (haystack.substring(i, needle.length + i) === needle) return i;
  }
  return -1;
};

// const res = strStr("sadbutsad", "sad");
// console.log(res);

// const res2 = strStr("leetcode", "leeto");
// console.log(res2);

const res3 = strStr("hello", "ll");
console.log(res3);

// Given a string needle and a string haystack
// iterate through haystack
// if the substring from current index to needle length equals the needle
// return current index
// after iteration return -1
