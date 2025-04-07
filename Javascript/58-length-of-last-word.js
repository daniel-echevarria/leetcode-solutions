var lengthOfLastWord = function (s) {
  const wordArray = s.split(" ").filter((x) => x !== "");
  const n = wordArray.length;
  return wordArray[n - 1].length;
};

const res = lengthOfLastWord("   fly me   to   the moon  ");

console.log(res);

// Algo
// split the string into array of words
// remove the empty strings
// return length of the last word
