var wordPattern = function (pattern, s) {
  const hash = new Map();
  const words = s.split(" ");
  if (!(words.length === pattern.length)) return false;
  words.forEach((word, i) => {
    const key = word;
    const value = pattern[i];
    const storedValues = [...hash.values()];
    if (!(hash.has(key) || storedValues.includes(value))) hash.set(key, value);
  });
  const decoded = words.map((w) => hash.get(w));
  const isMatch = decoded.join("") === pattern;
  return isMatch;
};

console.log(wordPattern("abba", "dog cat cat dog"));

// Algo wordPattern
// given a pattern and a string
// split the string into an array of words
// map each word of the string to a letter in the pattern
// unless the map already has the key or the value already exists in the map
// after mapping reconstruct the pattern from the string
// if they match return true otherwise return false
