const romanMap = {
  1: "I",
  4: "IV",
  5: "V",
  9: "IX",
  10: "X",
  40: "XL",
  50: "L",
  90: "XC",
  100: "C",
  400: "CD",
  500: "D",
  900: "CM",
  1000: "M",
};

const findTheHighestSymbol = (int, romanMap) => {
  const keysArray = Object.keys(romanMap);
  let h = keysArray[0];
  keysArray.forEach((key) => {
    if (int - key < 0) return;
    h = key;
  });
  return h;
};

var intToRoman = function (num) {
  const result = convert(num);
  return result;
};

const convert = (val, result = []) => {
  if (val === 0) return result.join("");
  const highest = findTheHighestSymbol(val, romanMap);
  result.push(romanMap[highest]);
  val -= highest;
  return convert(val, result);
};

const rom = intToRoman(3749);
const rom2 = intToRoman(1994);
console.log(rom2);

// intToRoman Algo
// Given an integer
// declare a romanMap with all the translations
// declare an empty array result
// map the integer to an array decimals (for example 393 becomes 300 90 3)
// For each value call convert

// Convert Algo
// if the value is 0 return
// find the highest possible element one can subtract
// Add that symbol to the result array and remove the value from the current value
// call convert with the rest
// return joined result

// console.log(findTheHighestSymbol(400, romanMap));

// Algo findTheHighestSymbol
// Given an integer
// declare a variable h with an initial value of the first element of the keys
// Iterate through the keys of the romanMap
// if the integer - key is smaller than 0 return h
// h gets current key

// Map Algo
// Split the integer into an array of strings of length 1
// iterate through the array and add as many 0 as the length minus the index
