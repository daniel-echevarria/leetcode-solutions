var findSubstring = function (s, words) {
  const oneWordLength = words[0].length;
  let left = 0;
  let right = oneWordLength;
  let currentConCat = [];
  let lastEncounteredAt = new Map();
  const result = [];
  while (s.substring(left).length >= words.length) {
    const sub = s.substring(right - oneWordLength, right);
    const match = words.indexOf(sub, lastEncounteredAt.get(sub) || 0);
    if (match < 0) {
      left++;
      right = left + oneWordLength;
      currentConCat = [];
      lastEncounteredAt = new Map();
      continue;
    }
    currentConCat.push(match);
    lastEncounteredAt.set(sub, match + 1);
    if (currentConCat.length === words.length) {
      result.push(left);
      currentConCat = [];
      lastEncounteredAt = new Map();
      left++;
      right = left + oneWordLength;
    } else {
      right += oneWordLength;
    }
  }
  return result;
};

console.log(
  findSubstring("aaaaaaaaaaaaaaaaa", [
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
  ])
);

console.log(findSubstring("a", ["a"]));

console.log(findSubstring("barfoothefoobarman", ["foo", "bar"]));
console.log(findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "foo"]));
console.log(
  findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", [
    "fooo",
    "barr",
    "wing",
    "ding",
    "wing",
  ])
);

// Algo
// declare oneWordLength with an initial value of words[0]
// declare a variable left with initial value of 0
// declare a variable right with initial value of oneWordLength
// declare an empty array currentConCat
// declare a map lastEncounteredAt
// launch a loop
// look for the index of the substring(left, right)
// but if the substring is a key of the map search only from the value of that key (which is the index + 1)
// if the index is -1
// left gets right
// right gets right + oneWordLength
// otherwise push the index to currentConCat
// and add the sub as a key to the map with a value of the index + 1
// if currentConCat is the same length as words
// push left to result
// currentConCat gets an empty array
// left gets right
// right gets right + oneWordLength
// otherwise right gets + oneWordLength
// if the characters left are not enough to contain all the words
// return the result array
