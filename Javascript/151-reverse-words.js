var reverseWords = function (s) {
  const wordArray = s.split(" ").filter((x) => x !== "");
  const backwards = wordArray.reverse();
  return backwards.join(" ");
};

const res = reverseWords("  hello world  ");
console.log(res);

// Algo
// Given a string
// declare a result array
// split it into an array of words
// remove all empty strings
// reverse the array
// return a joined version with a space as a separator

// Algo reverseWord
// split word into array of letters
// return reverse the array and join
