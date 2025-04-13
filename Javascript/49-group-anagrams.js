var groupAnagrams = function (strs) {
  const groups = new Map();
  const result = [];
  let groupIndex = 0;
  strs.forEach((originalString) => {
    const key = originalString.split("").sort().join("");
    if (groups.has(key)) {
      const index = groups.get(key);
      result[index].push(originalString);
    } else {
      groups.set(key, groupIndex);
      result.push([originalString]);
      groupIndex++;
    }
  });
  return result;
};

// Algo groupAnagrams
// Declare a map groups
// declare an empty array result
// declare a variable groupIndex with an initial value of 0
// Iterate through the strings of strs
// for each string
// sort the string to a newString, look for the newString in the keys
// if one is found push the unsorted string to the nested array in result at the index indicated by the value of the key
// if none is found create a key with the sortedString with a value of groupIndex
// push to result an array with the unsorted string
// and add 1 to groupIndex
// after iteration return the result array

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
// console.log(groupAnagrams([""]));
// console.log(groupAnagrams(["a"]));
// console.log(groupAnagrams(["", ""]));
