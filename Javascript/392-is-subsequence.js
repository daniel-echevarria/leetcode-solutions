var isSubsequence = function (s, t) {
  if (s.length === 0) return true;
  const filtered = t
    .split("")
    .filter((x) => s.includes(x))
    .join("");
  let i = 0;
  let j = 0;
  while (i < s.length && j < filtered.length) {
    if (s[i] === filtered[j]) i++;
    if (i === s.length) return true;
    j++;
  }
  return false;
};

let res = isSubsequence("ab", "baab");
console.log(res);

res = isSubsequence("abc", "ahbgdc");
console.log(res);

res = isSubsequence("axc", "ahbgdc");
console.log(res);

// Given two strings
// create a filtered copy of t with only characters from s
// declare a variable i with an initial value of 0
// declare a variable j with an initial value of 0
// Loop while i is smaller than s length and j is smaller than t length
// compare s[i] with t[j]
// if they are the same i get +1
// if i equals s length return true
// j gets +1
// After loop  return false
