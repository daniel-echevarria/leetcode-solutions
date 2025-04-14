var isHappy = function (n) {
  return recurHappy(n);
};

const recurHappy = (n) => {
  const happy = [1, 7];
  const sad = [2, 3, 4, 5, 6, 8, 9];
  const sumOfDigits = n
    .toString()
    .split("")
    .map((x) => +x * +x)
    .reduce((acc, current) => acc + current);
  if (happy.includes(sumOfDigits)) return true;
  if (sad.includes(sumOfDigits)) return false;
  return recurHappy(sumOfDigits);
};

console.log(isHappy(19));
console.log(isHappy(2));

// Algo isHappy
// Given a number
// convert it to a string
// split the string into an array of characters
// map the array to an array of the numbers squared
// add all the elements in the array
// if the elements add to 1 or 7 return true
// if they add to 2,3,4,5,6,8,9 return false
// recursively call isHappy on the result
