var romanToInt = function (s) {
  const romanMap = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  const n = s.length;
  let total = 0;
  const romanArray = s.split("");
  const converted = romanArray.map((x) => romanMap[x]);
  for (let i = 1; i < n; i++) {
    const previous = converted[i - 1];
    const current = converted[i];
    total += previous >= current ? previous : -previous;
  }
  total += converted[n - 1];
  return total;
};

const result = romanToInt("MCMXCIV");
console.log(result);

// Given a roman numbers s
// create an hash map of the equivalence between roman symbols and their values
// declare a variable total with a initial value of 0
// split the string into an array of string of length 1
// convert each string to it's integer value
// loop through the array starting from index 1
// If the previous value is bigger add it to total
// otherwise remove it from total
// return total
