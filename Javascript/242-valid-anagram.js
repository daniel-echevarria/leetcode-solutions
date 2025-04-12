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
// console.log(isAnagram("anagram", "nagaram"));
// console.log(isAnagram("rat", "car"));
console.log(isAnagram("aacc", "ccac"));

// algo isAnagram
// given two strings s and t
// return false if s and t are not the same length
// iterate through s
// and map each letter to a number of appearances
// then iterate through t
// if the count of that letter is less than 1
// or there is no count for that letter return false
// otherwise remove 1 from the count of letter
