var isPalindrome = function (s) {
  const clean = s.replace(/[^a-zA-Z0-9]+/g, "").toLowerCase();
  const n = clean.length;
  const half = Math.floor((n - 1) / 2);
  for (let i = 0; i < half + 1; i++) {
    if (clean[i] !== clean[n - 1 - i]) return false;
  }
  return true;
};

const res = isPalindrome("A man, a plan, a canal: Panama");
console.log(res);

const res2 = isPalindrome("race a car");
console.log(res2);

const res3 = isPalindrome("0P");
console.log(res3);

// Algo isPalindrome
// Given a string
// split it into an array chars
// filter all the non letter characters
// make everything smaller case
// store the result in a variable clean
// declare a variable i with initial value 0
// declare a variable j with initial value of clean length
// iterate through clean until the half of the array + 1
// if clean[i] does not equal clean[j] return false
// after iteration return true
