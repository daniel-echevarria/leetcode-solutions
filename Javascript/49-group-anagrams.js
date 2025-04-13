// const isAnagram = (a, b) => {
//   const firstString = a.split("").sort().join("");
//   const secondString = b.split("").sort().join("");
//   return firstString === secondString;
// };

var isAnagram = function (s, t) {
  const hash = new Map();
  if (!(s.length === t.length)) return false;

  // Iterate through s and map each letter to a count
  for (let i = 0; i < s.length; i++) {
    const letter = s[i];
    hash.set(letter, (hash.get(letter) || 0) + 1);
  }

  // Iterate trough t and remove from the count
  for (let i = 0; i < t.length; i++) {
    const letter = t[i];
    if (!hash.has(letter) || hash.get(letter) < 1) return false;
    hash.set(letter, hash.get(letter) - 1);
  }

  return true;
};

var groupAnagrams = function (strs) {
  const groups = new Map();
  strs.forEach((s) => {
    const anagram = groups.keys().find((x) => isAnagram(x, s));
    if (anagram !== undefined) {
      const anagramGroupArray = groups.get(anagram);
      anagramGroupArray.push(s);
    } else {
      groups.set(s, []);
    }
  });
  const result = [];
  groups.keys().forEach((key) => {
    result.push([key, groups.get(key)].flat());
  });
  return result;
};

// console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
// console.log(groupAnagrams([""]));
// console.log(groupAnagrams(["a"]));
console.log(groupAnagrams(["", ""]));

// Algo groupAnagrams
// Declare a hashMap groups
// Iterate through the strings of strs
// for each string
// look for an anagram of the string in the map
// if one is found push the current string to the value array of that key
// if none is found create a key with that string with a value of an empty array
// after iteration
// declare a variable result with an empty array
// iterate through the keys of the map
// for each key, push to results the key together with the value as a flatten array
// after iteration return results

// Algo isAnagram
// Takes two strings
// return false if the strings do not have the same length
// split both strings into arrays of characters
// sort the arrays
// join the strings again
// see if they are the same
